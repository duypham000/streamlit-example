LABEL = """
Q: Give me title and key points this text, each key points, give a label negative, positive, info or advertisement:
Cổ phiếu VIC (Vingroup) đã có gần 2 tuần đi nganh vùng 43.x - 46.x với lực bán và thanh khoản giảm mạnh.
Kết tuần giao dịch giằng co từ 2 - 6/10, VN-Index giảm 26 điểm từ ngưỡng 1.154.
Chỉ sau 1 tháng kể từ thời điểm chinh phục bất thành cao điểm 1.250, thị trường chứng khoán đã mất gần 120 điểm (-9,36%); thanh khoản trong gần 2 tuần nay liên tục giảm mạnh về dưới 20.000 tỷ đồng/phiên cho thấy tâm lý nhà đầu tư vẫn đang rất thận trọng. 
VN-Index sau khi giảm về dưới hỗ trợ MA200 (ngưỡng 1.150 điểm) cũng bắt đầu ghi nhận lực bán giảm đáng kể. Tuy nhiên, bên mua vẫn tỏ ra thận trọng trước những diễn biến khó lường về vĩ mô.
Theo ông Nguyễn Đức Nhân - Giám đốc Kinh doanh Công ty Chứng khoán KB Việt Nam, thị trường chứng khoán đang có dấu hiệu tạo đáy lớn với thanh khoản cạn kiệt. Mặc dù vậy, VN-Index nhiều khả năng sẽ đi vào trạng thái tích lũy vùng giá quanh 1.115 điểm +/-5 điểm.
Nhịp điều chỉnh của thị trường thời gian qua có dấu ấn không nhỏ từ đà lao dốc của bộ 3 cổ phiếu nhà Vin trong đó VIC giảm gần 40% từ mức 75.600 đồng về 45.950 đồng/cp (giá kết phiên 6/10); VHM giảm 27% từ mức 62.900 đồng về 46.050 đồng/cp; VRE giảm 12% từ 31.300 đồng về 27.450 đồng/cp.
Tuần qua, kể từ thời điểm VN-Index điều chỉnh về dưới mốc 1.110 điểm, bộ 3 cổ phiếu nhóm Vingroup cũng xuất hiệu dấu hiệu tạo đáy. VIC đã có gần 2 tuần đi nganh trong vùng 43.x - 46.x (thấp nhất 6 năm) với lực bán và thanh khoản giảm mạnh.
Trong khi đó, cổ phiếu VRE đang là mã tiên phong trong việc hồi phục khi đã tăng 7,6% trong 6 phiên trở lại đây.
Ông Nhân cho rằng, dù nhà đầu tư không tham gia sở hữu nhóm cổ phiếu Vingroup tuy nhiên những vận động của họ cổ phiếu này vẫn là điều cần đáng lưu tâm.
Với việc bộ 3 VIC - VHM - VRE cho tín hiệu tạo đáy, thị trường chứng khoán nhiều khả năng sẽ dừng lại đà giảm điểm cùng với sự cộng hưởng khả quan các nhóm ngành. Dù vậy, sau nhịp giảm mạnh và tạo đáy, quá trình vận động tích lũy và đi lên của của các cổ phiếu sẽ không hề ngắn.
Trong quý 4/2023, việc cổ phiếu VIC có thể hồi phục trở lại ngưỡng 53.0 - 55.0 đã là thành công với cổ phiếu \"anh cả\" ngành bất động sản. Tuy nhiên với dự phóng này, VN-Index có cơ hội quay lại trở ngưỡng điểm bình thường như trước nhịp điều chỉnh.
Vietbank là ngân hàng đứng ra thu xếp tài chính cho các doanh nghiệp trong “hệ sinh thái' Hoa Lâm.
Bệnh viện Quốc tế City thưởng Tết 250 triệu đồng/người, mức thưởng cao nhất hiện nay.
JSON: {
  "title": "VIC, VHM, VRE giảm mạnh, có dấu hiệu tạo đáy",
  "key_points": [
      {
        "label": "Negative",
        "text": "VIC giảm gần 40% từ mức 75.600 đồng về 45.950 đồng/cp"
      },
      {
        "label": "Positive",
        "text": "VHM tăng 27% từ mức 46.050 đồng lên tới 62.900 đồng/cp"
      },
      {
        "label": "Negative",
        "text": "VRE giảm 12% từ 31.300 đồng về 27.450 đồng/cp."
      },
      {
        "label": "Negative",
        "text": "VIC đã có gần 2 tuần đi nganh trong vùng 43.x - 46.x (thấp nhất 6 năm) với lực bán và thanh khoản giảm mạnh."
      },
      {
        "label": "Positive",
        "text": "VRE đang là mã tiên phong trong việc hồi phục khi đã tăng 7,6% trong 6 phiên trở lại đây."
      },
      {
        "label": "Info",
        "text": "Bệnh viện Quốc tế City thưởng Tết 250 triệu đồng/người, mức thưởng cao nhất hiện nay."
      },
      {
        "label": "Info",
        "text": "Vietbank là ngân hàng đứng ra thu xếp tài chính cho các doanh nghiệp trong “hệ sinh thái' Hoa Lâm."
      }
  ]
}
"""

ADS = """
Q: This text is ads or not:
Bệnh viện Quốc tế City thưởng Tết 250 triệu đồng/người, mức thưởng cao nhất hiện nay.Bệnh viện Quốc tế City (CIH) được khánh thành ngày 5/1/2014 với quy mô gần 500 nhân sự, 21 chuyên khoa, mũi nhọn gồm khoa Phụ sản và khoa Nhi, Tim mạch, Sức khỏe tổng quát.CIH được biết đến là thành viên trong 'hệ sinh thái' của Tập đoàn Hoa Lâm.Vietbank là ngân hàng đứng ra thu xếp tài chính cho các doanh nghiệp trong “hệ sinh thái' Hoa Lâm.
JSON: {"is_ads": 1}
Q: This text is ads or not:
Thanh khoản HPG đạt gần 1.500 tỷ đồng, chiếm 8% toàn sàn HoSE và là mức cao nhất kể từ đầu tháng 9.
Hôm nay, mã chứng khoán của Công ty cổ phần Tập đoàn Hòa Phát (HPG) ghi nhận giá trị giao dịch gần 1.500 tỷ đồng, cao nhất thị trường. Con số này tăng hơn 100 tỷ đồng so với hôm qua, giúp HPG có hai phiên liên tiếp giao dịch hơn nghìn tỷ đồng. Thanh khoản cổ phiếu này hiện cao nhất 3 tháng qua. Nếu xét về khối lượng giao dịch, gần 52,8 triệu cổ phiếu được sang tay hôm nay là mức cao nhất kể từ đầu tháng 8.
Về thị giá, HPG tăng mạnh chỉ sau gần một tiếng mở cửa, có lúc đạt 28.250 đồng một cổ phiếu, cao hơn 2,4% so với tham chiếu. Mã này duy trì vùng giá trên 28.000 đồng gần suốt buổi sáng trước khi hạ nhiệt ở phiên chiều. Sau cơn rung lắc những phút cuối, HPG đóng cửa ở 27.700 đồng, nhích thêm 0,4% so với hôm qua.
Nhà đầu tư giao dịch sôi nổi sau thông tin Tập đoàn Hòa Phát bán 709.000 tấn thép các loại trong tháng 11, tăng 12% so với tháng trước và 60% so với cùng kỳ năm ngoái. Riêng thép xây dựng và thép chất lượng cao tăng 63% so với cùng kỳ 2022.
Doanh nghiệp này cho biết, thị trường thép xây dựng trong nước tăng do bắt đầu vào mùa xây dựng và một phần đến từ các giải pháp thúc đẩy giải ngân vốn đầu tư công. Điều này dẫn đến việc tiêu thụ ở cả ba miền của Hòa Phát đều ghi nhận sự tăng trưởng. Trong đó, mức tăng cao nhất là khu vực phía Nam, cao hơn 47% so với tháng trước.
Riêng mã HPG đã chiếm hơn 8% thanh khoản toàn sàn HoSE. Tổng giá trị giao dịch ở thị trường này đạt hơn 17.700 tỷ đồng, giảm hơn 9.700 tỷ so với hôm qua. Dòng tiền của nhà đầu tư tập trung vào nhóm bất động sản, chứng khoán và tài nguyên.
JSON: {"is_ads": 0}
"""
