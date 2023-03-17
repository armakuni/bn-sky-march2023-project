package com.example.Catalog_API.catalog;

import jakarta.persistence.*;

@Entity(name = "products")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column (name = "product_id")
    private int id;

    @Column(name = "productName")
    private String productName;

    @Column(name = "price")
    private int price;
    
    @Column(name = "quantity")
    private int quantity;
  
    @Column(name = "imageurl")
    private String imageurl;

    //Constructor
    public Product(String productName,int price, int quantity) {
        this.productName = productName;
        this.price = price;
        this.quantity = quantity;
        this.imageurl = new String();
    }

    //Empty constructor
    public Product(){}

    //Getters and Setters
     public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return productName;
    }

    public void setName(String productName) {
        this.productName = productName;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public String getImageUrl() {
        return imageurl;
    }

    public void setImageUrl(String imageurl) {
        this.imageurl = imageurl;
    }

}


