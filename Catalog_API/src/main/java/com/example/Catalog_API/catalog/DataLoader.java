package com.example.Catalog_API.catalog;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

@Component
public class DataLoader implements ApplicationRunner {
    @Autowired
    ProductRepository productRepository;

    public DataLoader(){}


    @Override
    public void run(ApplicationArguments args) throws Exception {

    Product yoyo = new Product( "Yoyo", 25);
    Product kazoo = new Product( "Kazoo", 20);
    Product glockenspiel = new Product( "Glockenspiel", 10);
    Product banjo = new Product( "Banjo", 15);
    Product chair = new Product( "Herman Miller", 30);
    Product painting = new Product( "Monet Print", 500);
    Product toy = new Product( "Newtons Cradle", 250);
    Product gadget = new Product( "Plasma Lamp" , 25);
    Product kitchenAppliance = new Product( "Air Fryer", 1000);
    Product shoes = new Product( "Converse", 60);

    productRepository.save(yoyo);
    productRepository.save(kazoo);
    productRepository.save(glockenspiel);
    productRepository.save(banjo);
    productRepository.save(chair);
    productRepository.save(painting);
    productRepository.save(toy);
    productRepository.save(gadget);
    productRepository.save(kitchenAppliance);
    productRepository.save(shoes);

    }
}