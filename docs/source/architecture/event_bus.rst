*********
Event Bus
*********

Intro
=====

The Event Bus is one of realization publish-subscribe pattern. Publish–subscribe
is a messaging pattern where senders of messages, called publishers, do not
program the messages to be sent directly to specific receivers, called
subscribers, but instead categorize published messages into classes without
knowledge of which subscribers, if any, there may be. Similarly, subscribers
express interest in one or more classes and only receive messages that are of
interest, without knowledge of which publishers, if any, there are. See more
information in 
`WIKI <https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern?>`_.

Event Bus concept in Alix project
=================================

The component diagram located follow. The event bus contain two core components
(API and EventFilter). API component is provide interface to subscribe and fire
events. The event bus create event queue for every event subscribers. The
EventFilter is filtering events and put events to target queues.

.. uml:: diagrams/event_bus/components.puml
    :align: center

Event Bus interface
-------------------

The event bus has two API methods for subscribing and firing events. The first
is a subscribe method. The subscribe method accept EventType parameter and
returns a Queue if no errors. All events equals with passed event type will be
posted to this queue. A subscriber should check the queue on new events for
itself. Only new events will be posted to the queue after a subscriber subscribe
on a event. The second is a fire method. The fire method accept event object and
returns none if no errors. The below in sequence section you can see more
information about this methods.

.. uml:: diagrams/event_bus/interface.puml
    :align: center

Sequence diagrams
-----------------

See below sequence diagram for subscribe method.

.. uml:: diagrams/event_bus/subscribe_seq.puml
    :align: center

See below sequence diagram for fire method.

.. uml:: diagrams/event_bus/fire_seq.puml
    :align: center
