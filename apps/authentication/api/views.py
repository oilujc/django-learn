

from rest_framework import generics, permissions, viewsets
from django_filters import FilterSet, filters
from django.db.models import Q

from rest_framework.response import Response


from apps.authentication.models import Interest, TimelineItem
from apps.authentication.api.serializers import UserInterestSerializer, InterestSerializer, TimelineItemSerializer



class InterestFilter(FilterSet):
    search = filters.CharFilter(method='search_filter')

    class Meta:
        model = Interest
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(interest__icontains=value) |
            Q(translation__icontains=value)
        )

class InterestViewset(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Interest.objects.all()
        filterset = InterestFilter(request.GET, queryset=queryset)

        queryset = filterset.qs

        serializer = InterestSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserInterestSerializer(data=request.data, context={'request': request})


        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class TimelineItemListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TimelineItemSerializer

    def get_queryset(self):
        return TimelineItem.objects.filter(user=self.request.user).order_by('-created_at')
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
