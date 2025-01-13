from models.repos.media_type_repo import MediaTypeRepo

def view_media_type():
    """Fetches and displays all media types."""
    try:
        mtr = MediaTypeRepo()
        gamt = mtr.get_all_media_types()
        if not gamt:
            print("No media types found.")
        else:
            for li in gamt:
                print(f"Id: {li.media_type_id}, Name: {li.media_type_name}")
    except Exception as e:
        print(f"An error occurred: {e}")



def view_media_type_by_id(mt_id: int):
    """Fetches and displays a media type by ID."""
    try:
        mtr = MediaTypeRepo()
        mt = mtr.get_media_type(mt_id)
        if mt:
            print(f"Id: {mt.media_type_id}, Name: {mt.media_type_name}")
        else:
            print(f"No media type found with ID {mt_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_media_type_by_id(mt_id):
    """Deletes a genre type by ID."""
    try:
        gtr = MediaTypeRepo()
        gtr.delete_media_type(mt_id)
        print(f"Media type with ID {mt_id} deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



def delete_media_type_by_id(mt_id):
    """Deletes a media type by ID."""
    try:
        gtr = MediaTypeRepo()
        gtr.delete_media_type(mt_id)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all Media types")
    print("2. View genre Media by ID")
    print("3. Delete genre Media by ID")
    choice = input("Enter your choice: ").strip()  # Stripping any extra spaces from input

    if choice == "1":
        view_media_type()
    elif choice == "2":
        try:
            mt_id = int(input("Enter Media Type ID: "))
            view_media_type_by_id(mt_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    elif choice == "3":
        try:
            mt_id = int(input("Enter Media Type ID: "))
            delete_media_type_by_id(mt_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")        
    else:
        print("Invalid choice. Please choose 1, 2 or 3.")
