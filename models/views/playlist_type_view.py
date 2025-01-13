from models.repos.playlist_type_repo import PlaylistTypeRepo

def view_playlist_type():
    """Fetches and displays all playlist types."""
    try:
        ptr = PlaylistTypeRepo()
        gapt = ptr.get_all_playlist_types()
        if not gapt:
            print("No playlist types found.")
        else:
            for li in gapt:
                print(f"Id: {li.playlist_id}, Name: {li.playlist_name}")
    except Exception as e:
        print(f"An error occurred: {e}")



def view_playlist_type_by_id(pt_id: int):
    """Fetches and displays a playlist type by ID."""
    try:
        ptr = PlaylistTypeRepo()
        pt = ptr.get_playlist_type(pt_id)
        if pt:
            print(f"Id: {pt.playlist_id}, Name: {pt.playlist_name}")
        else:
            print(f"No playlist type found with ID {pt_id}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_playlist_type_by_id(pt_id):
    """Deletes a playlist type by ID."""
    try:
        ptr = PlaylistTypeRepo()
        ptr.delete_playlist_type(pt_id)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. View all playlist types")
    print("2. View playlist type by ID")
    print("3. Delete playlist type by ID")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_playlist_type()
    elif choice == "2":
        try:
            pt_id = int(input("Enter Playlist Type ID: "))
            view_playlist_type_by_id(pt_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
    elif choice == "3":
        try:
            pt_id = int(input("Enter Media Type ID: "))
            delete_playlist_type_by_id(pt_id)
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")        
    else:
        print("Invalid choice. Please choose 1, 2 or 3.")
