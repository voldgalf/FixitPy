import fixitpy

if __name__ == "__main__":
    found_guide = fixitpy.retrieve_guide(4000)  # call the retrieve_guide function which returns a dict

    print(f"Title: {found_guide.get("title")}")
    print(f"Difficulty: {found_guide.get("difficulty")}")
    print(f"Conclusion: {found_guide.get("conclusion")}")

    for step in found_guide.get("steps"):
        print(step.get("title"))
        print(step.get("text"))
        print(step.get("image_id"))