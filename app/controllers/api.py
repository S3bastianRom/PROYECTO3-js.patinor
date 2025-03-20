from flask import Blueprint, jsonify
from app.config.db import db
from app.models.ingrediente import Ingrediente
from app.models.producto import Producto
from app.models.producto_ingrediente import Producto_Ingrediente
from app.models.heladeria import Heladeria
from app.utils.decorators import roles_required

api_bp = Blueprint ("api", __name__, url_prefix= "/api")
#API Productos
@api_bp.route("/productos", methods=["GET"])
def api_productos():
    productos = Producto.query.all()
    return jsonify({
        "productos":
        [
            {
                "id": p.id,
                "nombre": p.nombre,
                "precio": p.precio
            } for p in productos]
    }), 200

#API Productos por ID
@api_bp.route("/productos/<int:id>", methods=["GET"])
def api_productos_id(id):
    productos = Producto.query.filter_by(id=id).first()
    return jsonify("producto",
    {
        "id": productos.id,
        "nombre": productos.nombre,
        "precio": productos.precio
    }),200

#API Productos por nombre
@api_bp.route("/productos/<nombre>", methods=["GET"])
def api_productos_name(nombre):
    productos = Producto.query.filter_by(nombre = nombre).first()
    return jsonify("producto",
    {
        "id": productos.id,
        "nombre": (productos.nombre).lower(),
        "precio": productos.precio
    }),200


#Calculo calorias API
@api_bp.route("/calcular_calorias/<int:id>", methods=["GET"])
@roles_required("cliente", "empleado", "admin")
def api_calcular_calorias(id):
    producto = Producto.query.filter_by(id=id).first()
    
    total = producto.calcular_calorias()
    return jsonify("calorias",
    {
        "nombre producto": (producto.nombre).lower(),
        "total calorias": total
    }), 200    

#Calculo rentabilidad API
@api_bp.route("/calcular_rentabilidad/<int:id>", methods=["GET"])
@roles_required("admin")
def api_calcular_rentabilidad(id):
    producto = Producto.query.filter_by(id=id).first()

    total_rentabilidad = producto.calcular_rentabilidad()
    return jsonify("rentabilidad",
    {
        "nombre producto": (producto.nombre).lower(),
        "rentabilidad": total_rentabilidad
    }),200

#Costo produccion API
@api_bp.route("/costo_produccion/<int:id>")
@roles_required("admin")
def api_costo_produccion(id):
    producto = Producto.query.filter_by(id=id).first()

    total_costo = producto.calcular_costo()
    return jsonify("costo_produccion",
    {
        "nombre producto": (producto.nombre).lower(),
        "rentabilidad": total_costo
    }),200


#Vender API
@api_bp.route("/vender/<int:id>")
@roles_required("cliente", "empleado", "admin")
def api_vender(id):
    heladeria = Heladeria.query.first()
    producto = Producto.query.get(id)
    
    try:
        heladeria.vender(producto.nombre)
        db.session.commit()
        return jsonify ("ventas",
        {
            "producto": (producto.nombre).lower(),
            "estado" : "vendido"
        }), 200
    except ValueError as e:
        db.session.rollback()
        return jsonify("ventas",
        {
            "producto": producto.nombre.lower(),
            "estado": "sin inventario",
            "detalle": str(e)
        }), 200
    

#API Ingredientes
@api_bp.route("/ingredientes", methods=["GET"])
@roles_required("admin")
def api_ingredientes():
    ingredientes = Ingrediente.query.all()
    return jsonify({
        "ingredientes":[
        {
            "id": i.id,
            "nombre": i.nombre,
            "precio": i.precio
        } for i in ingredientes]
    }),200


#API Ingredientes por ID
@api_bp.route("/ingredientes/<int:id>", methods=["GET"])
@roles_required("empleado", "admin")
def api_ingredientes_id(id):
    ingredientes = Ingrediente.query.filter_by(id=id).first()
    return jsonify("ingredientes",
    {
        "id": ingredientes.id,
        "nombre": ingredientes.nombre,
        "precio": ingredientes.precio
    }),200


#API Ingredientes por nombre
@api_bp.route("/ingredientes/<nombre>", methods=["GET"])
@roles_required("empleado", "admin")
def api_ingredientes_name(nombre):
    ingredientes  = Ingrediente.query.filter_by(nombre = nombre).first()
    return jsonify("ingredientes",
    {
        "id": ingredientes.id,
        "nombre": (ingredientes.nombre).lower(),
        "precio": ingredientes.precio
    }),200


#API Ingredientes es sano
@api_bp.route("/es_sano/<int:id>")
@roles_required("empleado", "admin")
def es_sano(id):
    ingrediente = Ingrediente.query.filter_by(id=id).first()
    
    try:
        sano = ingrediente.es_sano()
        return jsonify("ingrediente",
        {
            "ingrediente": ingrediente.id,
            "nombre": ingrediente.nombre,
            "es_sano": sano
        }),200

    except ValueError as e:
        return jsonify ("ingrediente",
        {
            "ingrediente": ingrediente.id,
            "nombre": ingrediente.nombre,
            "es_sano": str(e)
        }),400
    
#API abastecer
@api_bp.route("/abastecer/<int:id>")
@roles_required("empleado", "admin")
def abastecer(id):
    ingrediente = Ingrediente.query.filter_by(id=id).first()
    anterior_inventario = ingrediente.inventario

    ingrediente.abastecer()
    db.session.commit()
    
    return jsonify ("inventario",
    {
        "ingrediente": ingrediente.nombre,
        "tipo": ingrediente.tipo,
        "anterior_inventario": anterior_inventario,
        "nuevo_inventario": ingrediente.inventario
    }),200
        
#API renovacion
@api_bp.route("/renovacion/<int:id>")
@roles_required("empleado", "admin")
def renovar_complementos(id):
    ingrediente = Ingrediente.query.filter_by(id=id).first()
    anterior_inventario = ingrediente.inventario
    
    try:
        ingrediente.renovar_inventario()
        db.session.commit()
        return jsonify ("inventario",
        {
            "ingrediente": ingrediente.nombre,
            "tipo": ingrediente.tipo,
            "anterior_inventario": anterior_inventario,
            "nuevo_inventario": ingrediente.inventario
        }),200
    except ValueError as e:
        return jsonify ("inventario",
        {
            "ingrediente": ingrediente.nombre,
            "tipo": ingrediente.tipo
        }),200
