package com.example.Catalog_API.catalog;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ProductService {
    @Autowired
    ProductRepository productRepository;

    // Adding new product
    public Product addNewproduct(Product product){
        productRepository.save(product);
        return product;
    }

    //Deleting product
    public void deleteProduct(Long id){
    productRepository.deleteById(id);
    }

    //Get all products
    public List<Product>getAllProducts (){
        return productRepository.findAll();
    }

    //Getting product by Id
    public Optional<Product> getProductById (Long id){
        return productRepository.findById(id);
    }

    }