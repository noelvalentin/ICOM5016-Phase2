from flask import jsonify
from dao.groups import GroupsDAO

class GroupHandler:

    def build_group_chat_dict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        result['uid'] = row[2]
        return result

#--------------- Phase 2 ---------------#

    def getAllGroups(self):
        dao = GroupsDAO()
        group_list = dao.getAllGroups()
        result_list = []
        for row in group_list:
            result = self.build_group_chat_dict(row)
            result_list.append(result)
        return jsonify(Groups = result_list)

#----------------- END -----------------#

'''
    def getGroupById(self, gid):
        dao = GroupsDAO()
        row = dao.getGroupById(gid)
        if not row:
            return jsonify(Error = "Group Not Found"), 404
        else:
            group = self.build_group_chat_dict(row)
            return jsonify(Group = group)

    def getGroupByGroupName(self, gname):
        dao = GroupsDAO()
        group_list = dao.getGroupByGroupName(gname)
        result_list = []
        for row in group_list:
            result = self.build_group_chat_dict(row)
            result_list.append(result)
        return jsonify(Groups = result_list)

    def getAllGroupsByOwnerID(self, ownerID):
        dao = GroupsDAO()
        group_list = dao.getAllGroupsByOwnerID(ownerID)
        result_list = []
        for row in group_list:
            result = self.build_group_dict(row)
            result_list.append(result)
        return jsonify(Groups = result_list)
'''

'''
    def createGroup(self):
        dao = GroupsDAO()
        result = dao.createGroup()
        return result

    def deleteGroup(self, gid):
        dao = GroupsDAO()
        if not dao.getGroupById(gid):
            return jsonify(Error="Group not found."), 404
        result = dao.deleteGroup(gid)
        return result

    def updateGroup(self, gid):
        dao = GroupsDAO()
        if not dao.getGroupById(gid):
            return jsonify(Error="Group not found."), 404
        result = dao.updateGroup(gid)
        return result
'''
