package controllers

import play.api.libs.json._
import play.api.mvc._
import javax.inject._


@Singleton
class CartController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  var cart: List[String] = List("TelefonKoszyk", "KomputerKoszyk", "KableKoszyk")

  def getAll: Action[AnyContent] = Action { implicit _: Request[AnyContent] =>
    Ok(Json.toJson(cart))
  }

  def getProductByIndex(index: Int): Action[AnyContent] = Action { implicit _: Request[AnyContent] =>
    if (index >= 0){
      if (index < cart.length) {
      Ok(Json.toJson(cart(index)))
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
    cart = cart ++ List(product)
    Created("Product added")
  }

  def updateProductByIndex(index: Int): Action[JsValue] = Action(parse.json) { implicit request =>
    if (index >= 0) {
      if(index < cart.length) {
        val updateValue = (request.body \ "product").as[String]
        cart = cart.updated(index, updateValue)
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
      if (index < cart.length) {
        cart = cart.take(index) ++ cart.drop(index + 1)
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



