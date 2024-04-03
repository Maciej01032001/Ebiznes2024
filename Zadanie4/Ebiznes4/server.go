package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type Product struct {
	gorm.Model
	Name  string
	Price float64
}

func main() {
	echoHandler := echo.New()

	productsDb, errorMessage := gorm.Open(sqlite.Open("products.db"), &gorm.Config{})
	if errorMessage != nil {
		echoHandler.Logger.Fatal(errorMessage)
	}

	errorMessage = productsDb.AutoMigrate(&Product{})
	if errorMessage != nil {
		echoHandler.Logger.Fatal(errorMessage)
	}

	echoHandler.GET("/products", crudProductGetAll(productsDb))
	echoHandler.GET("/products/:id", crudProductGetOne(productsDb))
	echoHandler.POST("/products", crudProductCreate(productsDb))
	echoHandler.PUT("/products/:id", crudProductUpdate(productsDb))
	echoHandler.DELETE("/products/:id", crudProductDelete(productsDb))

	echoHandler.Logger.Fatal(echoHandler.Start(":1323"))
}

func crudProductGetAll(dataBase *gorm.DB) echo.HandlerFunc {
	return func(context echo.Context) error {

		var products []Product

		if errorMessage := dataBase.Find(&products).Error; errorMessage != nil {
			return context.JSON(http.StatusInternalServerError, errorMessage)
		}

		return context.JSON(http.StatusOK, products)
	}
}

func crudProductGetOne(dataBase *gorm.DB) echo.HandlerFunc {
	return func(context echo.Context) error {

		var product Product

		if errorMessage := dataBase.First(&product, context.Param("id")).Error; errorMessage != nil {
			return context.JSON(http.StatusNotFound, errorMessage)
		}

		return context.JSON(http.StatusOK, product)
	}
}

func crudProductCreate(dataBase *gorm.DB) echo.HandlerFunc {
	return func(context echo.Context) error {

		var product Product

		if errorMessage := context.Bind(&product); errorMessage != nil {
			return context.JSON(http.StatusInternalServerError, errorMessage)
		}

		if errorMessage := dataBase.Create(&product).Error; errorMessage != nil {
			return context.JSON(http.StatusInternalServerError, errorMessage)
		}

		return context.JSON(http.StatusCreated, product)
	}
}

func crudProductUpdate(dataBase *gorm.DB) echo.HandlerFunc {
	return func(context echo.Context) error {

		var product Product

		if errorMessage := context.Bind(&product); errorMessage != nil {
			return context.JSON(http.StatusInternalServerError, errorMessage)
		}

		if errorMessage := dataBase.Model(&Product{}).Where("id = ?", context.Param("id")).Updates(product).Error; errorMessage != nil {
			return context.JSON(http.StatusNotFound, errorMessage)
		}

		return context.JSON(http.StatusOK, product)
	}
}

func crudProductDelete(dataBase *gorm.DB) echo.HandlerFunc {
	return func(context echo.Context) error {

		if errorMessage := dataBase.Delete(&Product{}, context.Param("id")).Error; errorMessage != nil {
			return context.JSON(http.StatusNotFound, errorMessage)
		}

		return context.NoContent(http.StatusNoContent)
	}
}
