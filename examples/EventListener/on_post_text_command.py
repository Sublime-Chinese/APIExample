# coding:utf-8
"""
Class : sublime_plugin.EventListener
Methods : on_post_text_command(view, command_name, args)
Return Value : None
Description : Called after a text command has been executed.
"""


import sublime
import sublime_plugin


class EventListenerOnPostTextCommandCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        pass
