package controllers

import play.api.libs.json._
import play.api.mvc._
import javax.inject._


@Singleton
class CategoryController @Inject()(val controllerComponents: ControllerComponents) extends BaseController {

  var category: List[String] = List("TelefonKategoria", "KomputerKategoria", "KableKategoria")

  def getAll: Action[AnyContent] = Action {
    implicit _: Request[AnyContent] =>
      Ok(Json.toJson(category))
  }

  def getProductByIndex(index: Int): Action[AnyContent] = Action {
    implicit _: Request[AnyContent] =>
      if (index >= 0) {
        if (index < category.length) {
          Ok(Json.toJson(category(index)))
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
    category = category ++ List(product)
    Created("Product added")
  }

  def updateProductByIndex(index: Int): Action[JsValue] = Action(parse.json) { implicit request =>
    if (index >= 0) {
      if(index < category.length) {
        val updateValue = (request.body \ "product").as[String]
        category = category.updated(index, updateValue)
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
      if (index < category.length) {
        category = category.take(index) ++ category.drop(index + 1)
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



