Usage
=====

.. warning::

   Remember to import fixitpy, as the example code assume it is already imported.

    .. code-block:: python

        import fixitpy

Getting Guides
--------------

Retrieving a guide from iFixit with fixitpy is simple, just call `retrieve_guide` with your specified guide ID.

.. code-block:: python

    guide = fixitpy.retrieve_guide(123)
    # 123 is an example and can be changed

the returned ``guide`` is a dictionary object, and can be accessed similarly to the example below:

.. code-block:: python
    :linenos:

    # importing and guide retrieval hidden for simplicity, but still required

    print(f"Title: {guide.get("title")}")
    print(f"Difficulty: {guide.get("difficulty")}")
    print(f"Conclusion: {guide.get("conclusion")}")

As the returned ``guide`` is a dictionary, getting all values is as easy as printing them:

.. code-block:: python

    # importing and guide retrieval hidden for simplicity, but still required
    print(guide)

Guide Steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^

What makes a guide, a guide is the inclusion of steps to follow. These are included in the returned dictionary as a list under the key ``steps``.
Each step is a dictionary with the keys: *text*, *title*, and *image_id*

.. hint::

   Every key in ``steps`` is a str, **except** image_id, which is a list.

Below is an example of iterating through each guide step:

.. code-block:: python
    :linenos:

    # importing and guide retrieval hidden for simplicity, but still required

    for step in guide.get("steps"):
        print(step.get("title"))
        print(step.get("text"))


Getting Media
--------------

Retrieving media from iFixit with fixitpy is simple, just call `retrieve_media` with your specified media ID.

.. code-block:: python

    media = fixitpy.retrieve_media(123)
    # 123 is an example and can be changed

the returned ``media`` is a dictionary object, and can be accessed similarly to the example below:

.. code-block:: python
    :linenos:

    # importing and media retrieval hidden for simplicity, but still required

    print(media.get("width"))
    print(media.get("height"))

As the returned ``media`` is a dictionary, getting all values is as easy as printing them:

.. code-block:: python

    # importing and media retrieval hidden for simplicity, but still required
    print(media)

Media Sizes
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``media`` dictionary does not contain the images themselves, but the URLs as otherwise it be computationally expensive to retrieve all the images.

``media`` contains a dictionary called **sizes**, which contains various urls to various image sizes

.. warning::

    ``sizes`` is not rigid, and the available image sizes with vary, with some exceptions.

.. code-block:: python
    :linenos:

    # importing and media retrieval hidden for simplicity, but still required

    sizes = media.get("sizes")

    # 'thumbnail' is a very common size for iFixit Media
    print(sizes.get("thumbnail"))
