from rest_framework import serializers
from .models import user, conversation, message
#child
class MessageSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = message
        fields = ['chat_group', 'sender', 'text', 'timestamp']
        read_only_fields= ['timestamp']
#parent
class ConversationSerializer(serializers.ModelSerializer):
    messages= MessageSerializer(many=True)
    class Meta:
        model= conversation
        fields = ['user', 'participants', 'created_at', 'messages', 'id']
        depth =2
    def create(self, validated_data):
        # retrieve the text from the message  dictionary
        msg_data= validated_data.pop('messages')
        # create the parent
        conv_instance= conversation.objects.create(**validated_data)

        #create the children(loop)
        for msg_item in msg_data:
            message.objects.create(chat_group=conv_instance, **msg_item)

        return conv_instance
        


        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields ='__all__'

