from flask import jsonify
from dao.reactions import ReactionsDAO

class ReactionHandler:

    def build_reaction_dict(self, row):
        result = {}
        result['mid'] = row[0]
        result['number_of_likes'] = row[1]
        result['number_of_dislkes'] = row[2]
        return result

    def getReactionsByMessageId(mid):
        dao = ReactionsDAO()
        reactions_list = dao.getReactionsByMessageId(mid)
        result_list = []
        for row in reactions_list:
            result = self.build_reaction_dict(row)
            result_list.append(result)
        return jsonify(Reactions = result_list)
