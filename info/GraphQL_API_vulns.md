## GraphQL Vulnerabilities

### Testing
Universal query: ```query{__typename}``` : If you send this to any GraphQL endpoint, it will include the string ```{"data": {"__typename": "query"}}``` somewhere in its response
every GraphQL endpoint has a reserved field called __typename that returns the queried object's type as a string

### When testing for GraphQL endpoints, you should look to send universal queries to the following locations:
- /graphql
- /api
- /api/graphql
- /graphql/api
- /graphql/graphql

### Exploits

- GraphQL introspection
    Introspection queries are special kinds of queries that allow you to learn about a GraphQL API’s schema, and they also help power GraphQL development tools <br>
    Disabling introspection in production is common in order to reduce the API’s attack surface. 
- Suggestions
    
- CSRF
