package com.example.Catalog_API.catalog;

import java.net.http.HttpResponse;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ProductService {
    private String db_api_url = "";
    
    @Autowired
    ProductRepository productRepository;

    // Adding new product
    public Product addNewproduct(Product product){
        // productRepository.save(product);
        
        HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("http://" + db_api_url + "/products"))
                    .method("POST"
                    , product)
                    .build();
            HttpResponse<String> response = null;

            Product responseProduct = null;
            
            try {
                response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());

                responseProduct = new Product(response.body().name, response.body().price, response.body().quantity,)
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        
    
        return ;
    }

    // Deleting product
    public void deleteProduct(int id){
            // productRepository.deleteById(id);
            HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("http://" + db_api_url + "/products?id=" + String.valueOf(id)))
            .method("DELETE"
            , null)
            .build();
        HttpResponse<String> response = null;

        try {
        response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException e) {
        e.printStackTrace();
        } catch (InterruptedException e) {
        e.printStackTrace();
        }
        return null;
    }

    //Get all products
    public List<Product>getAllProducts (){
        HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("http://" + db_api_url + "/products"))
                    .method("GET"
                    , null)
                    .build();
            HttpResponse<String> response = null;
            
            try {
                response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        return response.body();
    }

    //Getting product by Id
    public Optional<Product> getProductById (int id){
        HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create("http://" + db_api_url + "/products?id=" + String.valueOf(id)))
                    .method("GET"
                    , null)
                    .build();
            HttpResponse<String> response = null;
            
            try {
                response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
            } catch (IOException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        return response.body();
    }

}


   
