# Introduction
This lesson gives an overview of the different topics we will cover in this chapter. Also, we will learn what is a Tier & it’s components?

We'll cover the following
What Is A Tier?
I’ll begin the course by discussing different tiers involved in the software architectural landscape. This is like a bird’s eye view of the realm of software architecture & is important to be understood well.

This chapter will help us understand:

What is a Tier?
Why do software applications have different tiers? What is the need for them?
How do I decide how many tiers should my application have?
What Is A Tier? #
Think of a tier as a logical separation of components in an application or a service. And when I say separation, I mean physical separation at the component level, not the code level.

What do I mean by components?

Database
Backend application server
User interface
Messaging
Caching
These are the different components that make up a web service.



Now let’s have a look at the different types of tiers & their real-life examples.




# Single Tier Applicaiton
A single-tier application is an application where the user interface, backend business logic & the database all reside in the same machine.

advantages: ----
    1) No network latency
    2) data request is fast
    3) soley depends on the power of machine to gauge the real performance of a single-tier app.
    4) ensures data safety at the highest level as it remains in users system

disadvantages: ------
    1) business has no control over the application
    2) It is vulnerable to being reversed engineered(security is minimum)
    3) performance and look is inconsistent as it depends on the configuration of the user's machine.


# Two Tier Application
A Two-tier application involves a client and a server. The client would contain the user interface & the business logic in one machine. And the backend server would be the database running on a different machine. The database server is hosted by the business & has control over it.

advantages: ------
    1) Control over the data
    2) Application makes less calls to database only


# Three Tier Application
In a three-tier application, the user interface, application logic & the database all lie on different machines & thus have different tiers. They are physically separated.
So, if we take the example of a simple blog, the user interface would be written using Html, JavaScript, CSS, the backend application logic would run on a server like Apache & the database would be MySQL. A three-tier architecture works best for simple use cases.


# N-Tier Application : distributed applications
An N-tier application is an application which has more than three components involved.
What are those components?

* Cache
* Message queues for asynchronous behaviour
* Load balancers
* Search servers for searching through massive amounts of data
* Components involved in processing massive amounts of data
* Components running heterogeneous tech commonly known as web services etc.

### Why the need for so many tiers?
It's because of these below two:
* Single Responsibility Principle
* the Separation of Concerns

**Single Responsibility Principle** means giving one, just one responsibility to a component & letting it execute it with perfection. Be it saving data, running the application logic or ensuring the delivery of the messages throughout the system.
This approach gives us a lot of flexibility & makes management easier.

For instance, when upgrading a database server. Like when installing a new OS or a patch, it wouldn’t impact the other components of the service running & even if something amiss happens during the OS installation process, just the database component would go down. The application as a whole would still be up & would only impact the features requiring the database.

We can also have dedicated teams & code repositories for every component, thus keeping things cleaner.

Single responsibility principle is a reason, why I was never a fan of stored procedures.

Stored procedures enable us to add business logic to the database, which is a big no for me. What if in future we want to plug in a different database? Where do we take the business logic? To the new database? Or do we try to refactor the application code & squeeze in the stored procedure logic somewhere?

A database should not hold business logic, it should only take care of persisting the data. This is what the single responsibility principle is. And this is why we have separate tiers for separate components.

**Separation Of Concerns** kind of means the same thing, be concerned about your work only & stop worrying about the rest of the stuff.

These principles act at all the levels of the service, be it at the tier level or the code level.

Keeping the components separate makes them reusable. Different services can use the same database, the messaging server or any component as long as they are not tightly coupled with each other.

Having loosely coupled components is the way to go. The approach makes scaling the service easy in future when things grow beyond a certain level.


## Difference Between Layes and Tiers

``**`
**Note**: Don’t confuse tiers with the layers of the application. Some prefer to use them interchangeably. But in the industry layers of an application typically means the user interface layer, business layer, service layer, or the data access layer.
```

![https://www.educative.io/api/collection/6064040858091520/6411938009448448/page/6047815849476096/image/5802038963208192]

The layers mentioned in the illustration are at the code level. The difference between layers and tiers is that the layers represent the organization of the code and breaking it into components. Whereas, tiers involve physical separation of components.

All these layers together can be used in any tiered application. Be it single, two, three or N-tier. I’ll discuss these layers in detail in the course ahead.

Alright, now we have an understanding of tiers. Let’s zoom-in one notch & focus on web architecture.



## Different Tiers in Softeare Architecture Quiz

Let’s Test Your Understanding Of Different Tiers In Software Architecture

1
What is a tier?

A)
Logical separation of components in an application or a service. The components are the database, backend application server, user interface, messaging, caching.

B)
Logical separation at the code level like the user interface layer, business layer, service layer, data access layer etc.

C)
Just the database & the backend server component in an application.

D)
Both, a component & a layer, at the code level, constitute a tier in an application.


2
When should we choose a single tier architecture for our application?

A)
When we need control over the code & the behaviour of our application.

B)
When we do not want any network latency.

C)
When we need to ensure that the application has a consistent behaviour, look & feel for all its users.


Which of the following are the correct reasons to choose a two-tier architecture for our application?

A)
When we do not want anyone to have access to the code/business logic of our application.

B)
When we need to minimize the network latency.

C)
When we need control over data in our application.




Which of the following are correct reasons to choose a three-tier architecture for our application?

A)
When it’s ok to have high network latency.

B)
When we need control over the code/business logic of our application & want it to be secure.

C)
When we need control over data in our application.



Why do software applications have different tiers? Which of the following option(s) are correct?

A)
To assign dedicated roles/tasks to different components for a loosely coupled architecture.

B)
To make the management, maintenance of the system & the introduction of new features in the application easier.

C)
To keep the network latency as high as possible.



Do layers and tiers in an application have the same meaning?

A)
Yes!! They have the same meaning & can be used interchangeably.

B)
No!! Tiers & layers in software architecture have different meanings & cannot be used interchangeably.