# To retrieve objects from your database, construct a QuerySet via a Manager on your model class.

# A QuerySet represents a collection of objects from your database. It can have zero, one or many filters. 

# Filters narrow down the query results based on the given parameters. In SQL terms, a QuerySet equates to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT.

# Managers are accessible only via model classes, rather than from model instances, to enforce a separation between “table-level” operations and “record-level” operations.

# Retrieving all objects¶
# The simplest way to retrieve objects from a table is to get all of them. To do this, use the all() method on a Manager:

all_entries = Entry.objects.all()
# The all() method returns a QuerySet of all the objects in the database.

# Retrieving specific objects with filters¶
# The QuerySet returned by all() describes all objects in the database table. Usually, though, you’ll need to select only a subset of the complete set of objects.

# To create such a subset, you refine the initial QuerySet, adding filter conditions. The two most common ways to refine a QuerySet are:

# filter(**kwargs)
# Returns a new QuerySet containing objects that match the given lookup parameters.
# exclude(**kwargs)
# Returns a new QuerySet containing objects that do not match the given lookup parameters.
# The lookup parameters (**kwargs in the above function definitions) should be in the format described in Field lookups below.

# For example, to get a QuerySet of blog entries from the year 2006, use filter() like so:

Entry.objects.filter(pub_date__year=2006)
# With the default manager class, it is the same as:

Entry.objects.all().filter(pub_date__year=2006)



''''
Chaining filters¶
The result of refining a QuerySet is itself a QuerySet, so it’s possible to chain refinements together. For example:

>>> Entry.objects.filter(
...     headline__startswith='What'
... ).exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(
...     pub_date__gte=datetime.date(2005, 1, 30)
... )

'''


'''
Filtered QuerySets are unique¶
Each time you refine a QuerySet, you get a brand-new QuerySet that is in no way bound to the previous QuerySet. Each refinement creates a separate and distinct QuerySet that can be stored, used and reused.

Example:

>>> q1 = Entry.objects.filter(headline__startswith="What")
>>> q2 = q1.exclude(pub_date__gte=datetime.date.today())
>>> q3 = q1.filter(pub_date__gte=datetime.date.today())
These three QuerySets are separate. The first is a base QuerySet containing all entries that contain a headline starting with “What”. The second is a subset of the first, with an additional criteria that excludes records whose pub_date is today or in the future. The third is a subset of the first, with an additional criteria that selects only the records whose pub_date is today or in the future. 
The initial QuerySet (q1) is unaffected by the refinement process.

https://docs.djangoproject.com/en/4.0/ref/models/querysets/#when-querysets-are-evaluated
'''