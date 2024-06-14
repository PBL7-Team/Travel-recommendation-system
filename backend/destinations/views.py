from django.shortcuts import render

# Create your views here.

import rest_framework
from rest_framework import permissions

from .pagination import LargeResultsSetPagination
from .models import Destination
from .serializers import DestinationSerializer
import csv
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


class DestinationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    pagination_class = LargeResultsSetPagination

    @action(detail=False, methods=["post"], url_path="import")
    def import_from_csv(self, request):
        if "csv_file" not in request.FILES:
            return Response(
                {"error": "No CSV file found"}, status=status.HTTP_400_BAD_REQUEST
            )

        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith(".csv"):
            return Response(
                {"error": "Invalid file format. Please upload a CSV file"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            print("here")
            decoded_file = csv_file.read().decode("utf-8").splitlines()
            csv_data = [row for row in csv.DictReader(decoded_file)]
            for index, data in enumerate(csv_data):
                serializer = self.get_serializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(f"Invalid data at index {index}: {data}")
            return Response(
                {"message": "Data imported successfully"},
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @action(detail=False, methods=["post"], url_path="demo")
    def test_import_from_csv(self, request):
        data_dict = {
            "name": "Làng Bích Họa Cảnh Dương",
            "address": "Địa chỉ: Xã Cảnh Dương, Xã Cảnh Dương, Huyện Quảng Trạch, Quảng Bình",
            "tel": "",
            "Website": "",
            "description": "Cảnh Dương một xã ven biển trù phú với cảnh quan thơ mộng, nằm cạnh QL 1A, cách khu mộ Đại tướng Võ Nguyên Giáp khoảng 10km với gần 375 năm hình thành và phát triển. Đây là vùng đất địa linh nhân kiệt, một trong “bát danh hương” của Quảng Bình xưa; là làng quê giàu truyền thống khoa bảng, làng chiến đấu nổi tiếng thời chống Pháp với khẩu hiệu “rào làng chiến đấu”, hai lần được phong Anh hùng lực lượng vũ trang nhân dân. Với sản phẩm “làng bích họa” độc đáo, du khách sẽ ngỡ ngàng với cung đường bích họa bắt đầu từ Đình thờ Tổ cho đến đường ven biển. Những bức tranh tường, tranh 3D độc đáo được vẽ lên nhằm mô tả câu chuyện về quá trình hình thành, phát triển, truyền thống anh hùng trong kháng chiến, những nét đẹp bình dị của làng biển trù phú này.",
        }
        serializer = self.get_serializer(data=data_dict)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(
                {"message": "Data imported successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
