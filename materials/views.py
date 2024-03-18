from django.http import JsonResponse, HttpResponse
from .models import ProductMaterial, Warehouse
from django.views.decorators.csrf import csrf_exempt
from math import ceil


@csrf_exempt
def materials(request):
    if request.method == "POST":

        product_materials = {
            p.product_name: {
                "Mato": p.fabric,
                "Ip": p.yarn,
                "Tugma": p.button,
                "Zamok": p.zip,
            }
            for p in ProductMaterial.objects.all()
        }
        warehouses = [
            {
                "warehouse_id": w.id,
                "material_name": w.material_name,
                "remainder": w.remainder,
                "price": w.price,
            }
            for w in Warehouse.objects.all()
        ]
        data = []

        for product_name, materials in product_materials.items():
            product_qty = request.POST.get(product_name)
            if product_qty is None:
                continue
            product_qty = int(product_qty)
            product = {
                "product_name": product_name,
                "product_qty": product_qty,
                "product_materials": [],
            }

            for material_name, material_qty in materials.items():
                if not material_qty:
                    continue
                required = ceil(material_qty * product_qty)

                for warehouse in warehouses:
                    if not (
                        warehouse["material_name"] == material_name
                        and warehouse["remainder"] > 0
                    ):
                        continue

                    if warehouse["remainder"] >= required:
                        product["product_materials"].append(
                            {
                                "warehouse_id": warehouse["warehouse_id"],
                                "material_name": material_name,
                                "qty": required,
                                "price": warehouse["price"],
                            }
                        )
                        warehouse["remainder"] -= required
                        break
                    else:
                        product["product_materials"].append(
                            {
                                "warehouse_id": warehouse["warehouse_id"],
                                "material_name": material_name,
                                "qty": warehouse["remainder"],
                                "price": warehouse["price"],
                            }
                        )
                        required -= warehouse["remainder"]
                        warehouse["remainder"] = 0

                else:
                    product["product_materials"].append(
                        {
                            "warehouse_id": None,
                            "material_name": material_name,
                            "qty": required,
                            "price": None,
                        }
                    )

            data.append(product)
        return JsonResponse({"result": data})
    return HttpResponse("Wrong request, please use POST request")
