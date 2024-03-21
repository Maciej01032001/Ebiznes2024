package controllers

import play.api._
import play.api.libs.json._
import play.api.mvc._

import javax.inject._


@Singleton
class HomeController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  var products: List[String] = List("Telefon", "Komputer", "Kable")

  def index() = Action { implicit request: Request[AnyContent] =>
    Ok(Json.obj("products" -> products))
  }

  def getAll: Action[AnyContent] = Action { implicit _: Request[AnyContent] =>
    Ok(Json.toJson(products))
  }

  def getProductByIndex(index: Int): Action[AnyContent] = Action { implicit _: Request[AnyContent] =>
    if (index >= 0){
      if (index < products.length) {
        Ok(Json.toJson(products(index)))
      }
      else {
        NotFound("Index out of range")
      }
    } else {
      NotFound("Index must be at least 0")
    }
  }

  def addProduct: Action[JsValue] = Action(parse.json) { implicit request =>
    val product = (request.body \ "product").as[String]
    products = products ++ List(product)
    Created("Product added")
  }

  def updateProductByIndex(index: Int): Action[JsValue] = Action(parse.json) { implicit request =>
    if (index >= 0) {
      if(index < products.length) {
        val updateValue = (request.body \ "product").as[String]
        products = products.updated(index, updateValue)
        Ok("Product updated")
      }
      else {
        NotFound("Index out of range")
      }
    }
    else {
      NotFound("Index must be at least 0")
    }
  }

  def deleteProductByIndex(index: Int): Action[AnyContent] = Action { implicit _: Request[AnyContent] =>
    if (index >= 0) {
      if (index < products.length) {
        products = products.take(index) ++ products.drop(index + 1)
        Ok("Product found and deleted")
      }
      else {
        NotFound("Index out of range")
      }
    }
    else {
      NotFound("Index must be at least 0")
    }
  }

}



