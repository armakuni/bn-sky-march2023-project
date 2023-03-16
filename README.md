# Building our own shop

### Project vision
Our own shop letting customers browse a catalog of amazing items and select them to purchase.

### Requirements

```
As a customer
I can view a list of products with prices
So that I can find what I want to buy
```
```
As a customer
I can add an item which has stock to my cart
So that I can prepare to check out
```
```
As a shop admin
I can edit the list of products and prices
So that I control what's for sale
```
```
As a shop owner
I only want customers to be able to add available items to their cart
So that customers don't check out when there's no stock left to buy
```

```
As an SRE
I want to view a dashboard showing the state of the system
So that I can quickly diagnose problems if something goes wrong
```

### Technical requirements
1. Build this on AWS
1. It should use an AWS MySQL-compatible database
1. It should use Kubernetes to run application code
1. The database and Kubernetes cluster should be created using IaC
1. Application and database should deploy using Github Actions
