from all_final_trait_number import Traits
from get_collection_reveal_stats import Collection

from operator import itemgetter
import collections

from my_project.db_connector import DbWriter
import json


_all = Traits.all_trait_number()
current = Collection.basis_traits(Collection.get_collection_stats())



class add_things():

    def current(d_key, key):
        result2 = ""

        for dict_i in current:
            if dict_i.get(d_key) is not None:
                result = dict_i.get(d_key)
                if result.get(key.lower()) is not None:
                    result2 = result.get(key.lower())

        return result2


    def _all():

        traits_paired = {}

        for dict_item in _all:
            for d_key in dict_item.keys():
                if dict_item.get(d_key) is not None:
                    trait = dict_item.get(d_key)
                    for key in trait.keys():
                        result_all = trait.get(key)[0]
                        result_value = trait.get(key)[2]
                        result_current = add_things.current(d_key, key)
                        if result_current == "":
                            result_current = 0
                        leftover = result_all - result_current
                        if d_key in traits_paired:
                            traits_paired[d_key].update({ key : (result_all , result_current, leftover, result_value)})
                        else:
                            traits_paired[d_key] = { key : (result_all , result_current, leftover, result_value)}
        return traits_paired


if __name__ ==  '__main__':
    # DbWriter.traits_left(add_things._all())
    print(add_things._all())

    with open('whats-left.json', 'w') as fp:
        json.dump(add_things._all(), fp)