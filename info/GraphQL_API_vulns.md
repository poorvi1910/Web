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
    - Introspection queries are special kinds of queries that allow you to learn about a GraphQL API’s schema, and they also help power GraphQL development tools <br>
    Disabling introspection in production is common in order to reduce the API’s attack surface.

    - Introspection probe request
    ```
    {
        "query": "{__schema{queryType{name}}}"
    }
    ```

    - If introspection is enabled but the above query doesn't run, try removing the onOperation, onFragment, and onField directives from the query structure. Many endpoints do not accept these directives as part of an introspection query, and you can often have more success with introspection by removing them.
 
    - **GraphQl visualiser** (http://nathanrandal.com/graphql-visualizer/) helps inunderstanding the schema more easily
 
    - If you cannot get introspection queries to run for the API you are testing, try inserting a special character after the __schema keyword.

      When developers disable introspection, they could use a regex to exclude the __schema keyword in queries. You should try characters like spaces, new lines and commas, as they are ignored by GraphQL but not by **flawed regex**.

      As such, if the developer has only excluded __schema{, then the below introspection query would not be excluded.
      ```
          #Introspection query with newline
        {
            "query": "query{__schema
            {queryType{name}}}"
        }
      ```

    - **URL encoded**
     ```
     # Introspection probe as GET request

    GET /graphql?query=query%7B__schema%0A%7BqueryType%7Bname%7D%7D%7D
     ```
  
- Suggestions

    Suggestions are a feature of the Apollo GraphQL platform in which the server can suggest query amendments in error messages. <br>
  These are generally used where a query is slightly incorrect but still recognizable (for example, There is no entry for 'productInfo'. Did you mean 'productInformation' instead?).

You can potentially glean useful information from this, as the response is effectively giving away valid parts of the schema.
Clairvoyance (https://github.com/nikitastupin/clairvoyance) is a tool that uses sugegstions to get the schea even when introspection is disabled

- Brute forcing using aliases
  Ordinarily, GraphQL objects can't contain multiple properties with the same name. Aliases enable you to bypass this restriction by explicitly naming the properties you want the API to return
  The simplified example below shows a series of aliased queries checking whether store discount codes are valid. This operation could potentially bypass rate limiting as it is a single HTTP request, even though it could potentially be used to check a vast number of discount codes at once.
    ```

    #Request with aliased queries

    query isValidDiscount($code: Int) {
        isvalidDiscount(code:$code){
            valid
        }
        isValidDiscount2:isValidDiscount(code:$code){
            valid
        }
        isValidDiscount3:isValidDiscount(code:$code){
            valid
        }
    }
    ```

- CSRF
    POST requests that use a content type of application/json are secure against forgery as long as the content type is validated.
  https://portswigger.net/web-security/graphql. But alternative methods such as GET, or any request that has a content type of ```x-www-form-urlencoded```, can be sent by a browser and so may leave users vulnerable to attack if the endpoint accepts these requests
