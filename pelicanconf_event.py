#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import json

EVENT_TITLE = "PyconES 2022"
EVENT_SUBTITLE = "Granada"
EVENT_DESCRIPTION = """
Bienvenidos a la PyConES, la conferencia nacional sobre Python más importante de España.<br>
Un evento de tres días que reunirá a los ponentes más interesantes, una agenda increíble y unas oportunidades de trabajo
maravillosas.<br>
Con tu entrada podrás acceder los dos días de la conferencia completos.<br>
Tambien puedes formar parte de nuestros patrocinadores y tener tu espacio dentro del evento.
"""

EVENT_TRACKS = json.dumps([
     { "id": 'a', "title": 'Room A' },
     { "id": 'b', "title": 'Room B', "eventColor": 'green' },
     { "id": 'c', "title": 'Room C', "eventColor": 'orange' },
     { "id": 'd', "title": 'Room D', "eventColor": 'red' }
])

EVENT_START_DATE = "2020-09-07"
EVENT_TALKS = json.dumps(
    [
       {
          "id":"1",
          "resourceId":"a",
          "start":"2020-09-07T09:00:00",
          "end":"2020-09-07T14:00:00",
          "title":"event 2",
          "editable":False,
          "description":"Ejemplo de descripción",
          "url":"https://stackoverflow.com/"
       },
       {
          "id":"2",
          "resourceId":"b",
          "start":"2020-09-08T09:00:00",
          "end":"2020-09-08T10:00:00",
          "title":"event 3",
          "editable":False
       },
       {
          "id":"3",
          "resourceId":"c",
          "start":"2020-09-07T07:30:00",
          "end":"2020-09-07T09:30:00",
          "title":"event 4",
          "editable":False
       },
       {
          "id":"4",
          "resourceId":"d",
          "start":"2020-09-07T10:00:00",
          "end":"2020-09-07T15:00:00",
          "title":"event 5",
          "editable":False
       }
    ]
)