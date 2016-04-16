from rest_framework import serializers


class CommandSerializer(serializers.Serializer):
    """This is the serializer for the commands that we receive through the Rest API.
    The command is a JSON object that we then will pass on to the associated container
    and the container executes the command.
    """
    code = serializers.CharField()
    target = serializers.CharField(required=False, allow_blank=True)
    container = serializers.CharField()


