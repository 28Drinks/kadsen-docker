import requests

from my_project.db_connector import DbWriter



class Collection():
    def get_collection_stats():

        all_traits = []

        url = "https://api.opensea.io/api/v1/collection/sportsbots"

        response = requests.get(url).json()


        all_traits.append(response["collection"]["traits"])


        return all_traits

    def basis_traits(data):

        basis_traits = []

        basis_traits.append({ "Background" : data[0]["Background"]})
        basis_traits.append({ "Body" : data[0]["Body"]})
        basis_traits.append({ "Teeth" : data[0]["Teeth"]})
        basis_traits.append({ "Eyes" : data[0]["Eyes"]})


        return basis_traits


if __name__ == '__main__':
    Collection.basis_traits(Collection.get_collection_stats())