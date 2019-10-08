#!/usr/bin/python
#  Example data to make management root directory structure from REST API call flat.
#   Input:
#       {
#           "children": [
#               {
#                   "children": [
#                       {
#                           "id": 25,
#                           "name": "file-test1.txt",
#                           "type": "File",
#                           "version": "1522092718"
#                       },
#                       {
#                           "children": [
#                               {
#                                   "id": 27,
#                                   "name": "sub-file-test1.txt",
#                                   "type": "File",
#                                   "version": "1522096401"
#                               }
#                           ],
#                           "id": 28,
#                           "name": "dir1",
#                           "type": "Directory",
#                           "version": "1522187109"
#                       }
#                   ],
#                   "id": 29,
#                   "name": "C",
#                   "type": "Directory",
#                   "version": "1522187109"
#               },
#               {
#                   "children": [],
#                   "id": 30,
#                   "name": "de",
#                   "type": "Directory",
#                   "version": "1522187109"
#               }
#           ],
#           "id": 31,
#           "name": "errors",
#           "type": "Directory",
#           "version": "1522187109"
#       }

from ansible import errors

class FilterModule(object):
    data = []

    def filters(self):
        return {
            'flatten_management_root': self.traverse
        }

    def traverse(self, value):
        for x in value:
            self.flatten(x, None)
        return self.data

    def flatten(self, element, parent):
        if(parent):
            path = parent+'/'+element['name']
        else:
            path = element['name']
        self.data.append(
			{
				'name': element['name'],
                'type': element['type'].lower(),
                'path': path
			}
		)
        if 'children' in element:
            for child in element['children']:
                self.flatten(child, path)
