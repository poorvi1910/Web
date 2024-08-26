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

In this wehn we search for the code for book searching functionality, we’ll find it in class BookController method Index:
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
it directly concatenates our searchString GET parameter’s value into query.Where:
