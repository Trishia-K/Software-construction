# KOBUMANZI TRISHIA
# M24B23/011
# BSCS

## Microservices

Microservices refers to an architecture where a single application is composed of many loosely coupled and independent smaller services.

## Microservices at Netflix

The microservices architecture that Netflix uses is powered by public cloud from Amazon Web Services. Basically, this architecture breaks down Netflix's large software programs into smaller programs based on modularity and each service performs a specific task and manages its own data. The different microservices in Netflix include edge services, play back service, recommendation service, content discovery service, User authentication and authorization service, billing and payment service, search service, monitoring and logging service and others. These services run independently but communicate with each other through APIs. The architecture works in such a way that when a user sends a request, it reaches an API gateway and then calls the other microservices for required data and these microservices can also request the data from different microservices and tools like Istio are used to manage traffic between these services and Eureka to ensure dynamic communication. After that, a complete response for the API request is sent back to the endpoint. The main advantage of this architecture is that if one service breaks, Netflix engineers can isolate that one service and the others keep running ensuring uninterrupted service.

## Two other companies using Microservices.

1. **Amazon**

Amazon also uses microservices to run its large e-commerce platform. It breaks the huge system into services like product catalog service, order processing service, payments service, delivery service and others. There are different teams and each is responsible for developing and maintaining its microservice. This enables Amazon to be able to release so many updates in a day but without having to update everything at once.

2. **Uber**

Uber used to use a monolith system but it struggled to expand to many cities and therefore it decided to adopt the microservices system which allows them to handle many different operations in different cities at once. The microservices include payment processing, location tracking, ride matching, pricing and others. When a user requests a ride, the request goes through Uber's API gateway and is then it looks for the appropriate microservices. For example, the ride matching service finds nearby drivers then the pricing service calculates the fare and the payment service handles transactions.

## Companies that shifted from microservices to monolithic architecture and why.

1. **Amazon Prime Video**

Amazon Prime Video used to use microservices for its video monitoring system and then decided to go back to the monolith system because the microservices system became very expensive and complicated to maintain. Engineers at Amazon prime video found out that many small services communicating with each other created too much overhead and when they changed it reduced infrastructure costs by about 90%.

2. **Segment**

Segment is a customer data platform company. It had over 150 microservices but it also switched from that to a single application. Having many microservices made the system difficult to manage and debug. In order to simpliy development and reduce operational complexity, it returned to a monolithic architecture.
