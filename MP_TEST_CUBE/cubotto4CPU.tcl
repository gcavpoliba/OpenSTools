model BasicBuilder -ndm 3 -ndf 4
set pid [getPID]
set np [getNP]
nDMaterial ElasticIsotropic 1 126313.39879199999 0.2 1.932
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    node 1 -10.43019962310791 -5.0206298828125 4.999350547790527
}
if { $pid == 2 } {
    node 1 -10.43019962310791 -5.0206298828125 4.999350547790527
}
if { $pid == 3 } {
    node 1 -10.43019962310791 -5.0206298828125 4.999350547790527
}
if { $pid == 1 } {
    node 2 -10.43019962310791 -1.486672282218933 4.999350547790527
}
if { $pid == 2 } {
    node 2 -10.43019962310791 -1.486672282218933 4.999350547790527
}
if { $pid == 3 } {
    node 2 -10.43019962310791 -1.486672282218933 4.999350547790527
}
if { $pid == 1 } {
    node 3 -10.43019962310791 -1.486672282218933 0.0
}
if { $pid == 2 } {
    node 3 -10.43019962310791 -1.486672282218933 0.0
}
if { $pid == 1 } {
    node 4 -10.43019962310791 -5.0206298828125 0.0
}
if { $pid == 2 } {
    node 4 -10.43019962310791 -5.0206298828125 0.0
}
if { $pid == 1 } {
    node 5 -13.9641580581665 -5.0206298828125 4.999350547790527
}
if { $pid == 2 } {
    node 5 -13.9641580581665 -5.0206298828125 4.999350547790527
}
if { $pid == 1 } {
    node 6 -13.9641580581665 -1.486672282218933 4.999350547790527
}
if { $pid == 1 } {
    node 7 -13.9641580581665 -1.486672282218933 0.0
}
if { $pid == 1 } {
    node 8 -13.9641580581665 -5.0206298828125 0.0
}
if { $pid == 1 } {
    node 9 -10.43019962310791 -8.554587364196777 4.999350547790527
}
if { $pid == 2 } {
    node 9 -10.43019962310791 -8.554587364196777 4.999350547790527
}
if { $pid == 3 } {
    node 9 -10.43019962310791 -8.554587364196777 4.999350547790527
}
if { $pid == 1 } {
    node 10 -10.43019962310791 -8.554587364196777 0.0
}
if { $pid == 2 } {
    node 10 -10.43019962310791 -8.554587364196777 0.0
}
if { $pid == 1 } {
    node 11 -13.9641580581665 -8.554587364196777 4.999350547790527
}
if { $pid == 2 } {
    node 11 -13.9641580581665 -8.554587364196777 4.999350547790527
}
if { $pid == 1 } {
    node 12 -13.9641580581665 -8.554587364196777 0.0
}
if { $pid == 1 } {
    node 13 -10.43019962310791 -5.0206298828125 9.998701095581055
}
if { $pid == 2 } {
    node 13 -10.43019962310791 -5.0206298828125 9.998701095581055
}
if { $pid == 3 } {
    node 13 -10.43019962310791 -5.0206298828125 9.998701095581055
}
if { $pid == 1 } {
    node 14 -10.43019962310791 -1.486672282218933 9.998701095581055
}
if { $pid == 3 } {
    node 14 -10.43019962310791 -1.486672282218933 9.998701095581055
}
if { $pid == 1 } {
    node 15 -13.9641580581665 -5.0206298828125 9.998701095581055
}
if { $pid == 2 } {
    node 15 -13.9641580581665 -5.0206298828125 9.998701095581055
}
if { $pid == 1 } {
    node 16 -13.9641580581665 -1.486672282218933 9.998701095581055
}
if { $pid == 2 } {
    node 17 -10.43019962310791 -8.554587364196777 9.998701095581055
}
if { $pid == 3 } {
    node 17 -10.43019962310791 -8.554587364196777 9.998701095581055
}
if { $pid == 2 } {
    node 18 -13.9641580581665 -8.554587364196777 9.998701095581055
}
if { $pid == 2 } {
    node 19 -6.896242141723633 -5.0206298828125 4.999350547790527
}
if { $pid == 3 } {
    node 19 -6.896242141723633 -5.0206298828125 4.999350547790527
}
if { $pid == 2 } {
    node 20 -6.896242141723633 -1.486672282218933 4.999350547790527
}
if { $pid == 3 } {
    node 20 -6.896242141723633 -1.486672282218933 4.999350547790527
}
if { $pid == 2 } {
    node 21 -6.896242141723633 -1.486672282218933 0.0
}
if { $pid == 2 } {
    node 22 -6.896242141723633 -5.0206298828125 0.0
}
if { $pid == 2 } {
    node 23 -6.896242141723633 -8.554587364196777 4.999350547790527
}
if { $pid == 3 } {
    node 23 -6.896242141723633 -8.554587364196777 4.999350547790527
}
if { $pid == 2 } {
    node 24 -6.896242141723633 -8.554587364196777 0.0
}
if { $pid == 3 } {
    node 25 -6.896242141723633 -5.0206298828125 9.998701095581055
}
if { $pid == 3 } {
    node 26 -6.896242141723633 -1.486672282218933 9.998701095581055
}
if { $pid == 3 } {
    node 27 -6.896242141723633 -8.554587364196777 9.998701095581055
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    node 40 -6.896242141723633 -6.787608623504639 4.999350547790527
}
if { $pid == 3 } {
    node 40 -6.896242141723633 -6.787608623504639 4.999350547790527
}
if { $pid == 2 } {
    node 41 -10.43019962310791 -6.787608623504639 9.998701095581055
}
if { $pid == 3 } {
    node 41 -10.43019962310791 -6.787608623504639 9.998701095581055
}
if { $pid == 1 } {
    node 42 -10.43019962310791 -6.787608623504639 4.999350547790527
}
if { $pid == 2 } {
    node 42 -10.43019962310791 -6.787608623504639 4.999350547790527
}
if { $pid == 3 } {
    node 42 -10.43019962310791 -6.787608623504639 4.999350547790527
}
if { $pid == 1 } {
    node 43 -10.43019962310791 -6.787608623504639 0.0
}
if { $pid == 2 } {
    node 43 -10.43019962310791 -6.787608623504639 0.0
}
if { $pid == 1 } {
    node 44 -10.43019962310791 -3.253651082515717 9.998701095581055
}
if { $pid == 3 } {
    node 44 -10.43019962310791 -3.253651082515717 9.998701095581055
}
if { $pid == 1 } {
    node 45 -10.43019962310791 -8.554587364196777 2.499675273895264
}
if { $pid == 2 } {
    node 45 -10.43019962310791 -8.554587364196777 2.499675273895264
}
if { $pid == 1 } {
    node 46 -13.9641580581665 -6.787608623504639 4.999350547790527
}
if { $pid == 2 } {
    node 46 -13.9641580581665 -6.787608623504639 4.999350547790527
}
if { $pid == 3 } {
    node 55 -6.896242141723633 -3.253651082515717 9.998701095581055
}
if { $pid == 2 } {
    node 56 -6.896242141723633 -3.253651082515717 4.999350547790527
}
if { $pid == 3 } {
    node 56 -6.896242141723633 -3.253651082515717 4.999350547790527
}
if { $pid == 1 } {
    node 57 -10.43019962310791 -1.486672282218933 7.499025821685791
}
if { $pid == 3 } {
    node 57 -10.43019962310791 -1.486672282218933 7.499025821685791
}
if { $pid == 1 } {
    node 58 -10.43019962310791 -5.0206298828125 7.499025821685791
}
if { $pid == 2 } {
    node 58 -10.43019962310791 -5.0206298828125 7.499025821685791
}
if { $pid == 3 } {
    node 58 -10.43019962310791 -5.0206298828125 7.499025821685791
}
if { $pid == 1 } {
    node 59 -13.9641580581665 -3.253651082515717 9.998701095581055
}
if { $pid == 1 } {
    node 60 -13.9641580581665 -1.486672282218933 7.499025821685791
}
if { $pid == 3 } {
    node 69 -6.896242141723633 -6.787608623504639 9.998701095581055
}
if { $pid == 2 } {
    node 70 -10.43019962310791 -8.554587364196777 7.499025821685791
}
if { $pid == 3 } {
    node 70 -10.43019962310791 -8.554587364196777 7.499025821685791
}
if { $pid == 2 } {
    node 71 -13.9641580581665 -6.787608623504639 9.998701095581055
}
if { $pid == 2 } {
    node 72 -6.896242141723633 -1.486672282218933 2.499675273895264
}
if { $pid == 2 } {
    node 73 -13.9641580581665 -8.554587364196777 7.499025821685791
}
if { $pid == 2 } {
    node 74 -12.19717884063721 -8.554587364196777 9.998701095581055
}
if { $pid == 2 } {
    node 80 -6.896242141723633 -3.253651082515717 0.0
}
if { $pid == 2 } {
    node 81 -6.896242141723633 -5.0206298828125 2.499675273895264
}
if { $pid == 2 } {
    node 82 -8.663220882415771 -5.0206298828125 4.999350547790527
}
if { $pid == 3 } {
    node 82 -8.663220882415771 -5.0206298828125 4.999350547790527
}
if { $pid == 2 } {
    node 83 -8.663220882415771 -1.486672282218933 4.999350547790527
}
if { $pid == 3 } {
    node 83 -8.663220882415771 -1.486672282218933 4.999350547790527
}
if { $pid == 2 } {
    node 92 -6.896242141723633 -6.787608623504639 0.0
}
if { $pid == 3 } {
    node 93 -6.896242141723633 -8.554587364196777 7.499025821685791
}
if { $pid == 2 } {
    node 94 -6.896242141723633 -8.554587364196777 2.499675273895264
}
if { $pid == 2 } {
    node 95 -8.663220882415771 -8.554587364196777 4.999350547790527
}
if { $pid == 3 } {
    node 95 -8.663220882415771 -8.554587364196777 4.999350547790527
}
if { $pid == 3 } {
    node 96 -6.896242141723633 -1.486672282218933 7.499025821685791
}
if { $pid == 2 } {
    node 97 -8.663220882415771 -8.554587364196777 0.0
}
if { $pid == 3 } {
    node 103 -6.896242141723633 -5.0206298828125 7.499025821685791
}
if { $pid == 3 } {
    node 104 -8.663220882415771 -5.0206298828125 9.998701095581055
}
if { $pid == 3 } {
    node 105 -8.663220882415771 -1.486672282218933 9.998701095581055
}
if { $pid == 3 } {
    node 106 -8.663220882415771 -8.554587364196777 9.998701095581055
}
if { $pid == 1 } {
    node 115 -10.43019962310791 -3.253651082515717 4.999350547790527
}
if { $pid == 2 } {
    node 115 -10.43019962310791 -3.253651082515717 4.999350547790527
}
if { $pid == 3 } {
    node 115 -10.43019962310791 -3.253651082515717 4.999350547790527
}
if { $pid == 1 } {
    node 116 -10.43019962310791 -1.486672282218933 2.499675273895264
}
if { $pid == 2 } {
    node 116 -10.43019962310791 -1.486672282218933 2.499675273895264
}
if { $pid == 1 } {
    node 117 -10.43019962310791 -3.253651082515717 0.0
}
if { $pid == 2 } {
    node 117 -10.43019962310791 -3.253651082515717 0.0
}
if { $pid == 1 } {
    node 118 -10.43019962310791 -5.0206298828125 2.499675273895264
}
if { $pid == 2 } {
    node 118 -10.43019962310791 -5.0206298828125 2.499675273895264
}
if { $pid == 1 } {
    node 119 -13.9641580581665 -3.253651082515717 4.999350547790527
}
if { $pid == 1 } {
    node 120 -13.9641580581665 -1.486672282218933 2.499675273895264
}
if { $pid == 1 } {
    node 121 -13.9641580581665 -3.253651082515717 0.0
}
if { $pid == 1 } {
    node 122 -13.9641580581665 -5.0206298828125 2.499675273895264
}
if { $pid == 1 } {
    node 123 -12.19717884063721 -5.0206298828125 4.999350547790527
}
if { $pid == 2 } {
    node 123 -12.19717884063721 -5.0206298828125 4.999350547790527
}
if { $pid == 1 } {
    node 124 -12.19717884063721 -1.486672282218933 4.999350547790527
}
if { $pid == 1 } {
    node 125 -12.19717884063721 -1.486672282218933 0.0
}
if { $pid == 1 } {
    node 126 -12.19717884063721 -5.0206298828125 0.0
}
if { $pid == 1 } {
    node 127 -13.9641580581665 -6.787608623504639 0.0
}
if { $pid == 1 } {
    node 128 -13.9641580581665 -8.554587364196777 2.499675273895264
}
if { $pid == 1 } {
    node 129 -12.19717884063721 -8.554587364196777 4.999350547790527
}
if { $pid == 2 } {
    node 129 -12.19717884063721 -8.554587364196777 4.999350547790527
}
if { $pid == 1 } {
    node 130 -12.19717884063721 -8.554587364196777 0.0
}
if { $pid == 1 } {
    node 131 -13.9641580581665 -5.0206298828125 7.499025821685791
}
if { $pid == 2 } {
    node 131 -13.9641580581665 -5.0206298828125 7.499025821685791
}
if { $pid == 1 } {
    node 132 -12.19717884063721 -5.0206298828125 9.998701095581055
}
if { $pid == 2 } {
    node 132 -12.19717884063721 -5.0206298828125 9.998701095581055
}
if { $pid == 1 } {
    node 133 -12.19717884063721 -1.486672282218933 9.998701095581055
}
if { $pid == 2 } {
    node 134 -8.663220882415771 -1.486672282218933 0.0
}
if { $pid == 2 } {
    node 135 -8.663220882415771 -5.0206298828125 0.0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 0 } {
    node 2 -10.43019962310791 -1.486672282218933 4.999350547790527
    node 3 -10.43019962310791 -1.486672282218933 0.0
    node 4 -10.43019962310791 -5.0206298828125 0.0
    node 5 -13.9641580581665 -5.0206298828125 4.999350547790527
    node 6 -13.9641580581665 -1.486672282218933 4.999350547790527
    node 7 -13.9641580581665 -1.486672282218933 0.0
    node 8 -13.9641580581665 -5.0206298828125 0.0
    node 9 -10.43019962310791 -8.554587364196777 4.999350547790527
    node 10 -10.43019962310791 -8.554587364196777 0.0
    node 11 -13.9641580581665 -8.554587364196777 4.999350547790527
    node 12 -13.9641580581665 -8.554587364196777 0.0
    node 13 -10.43019962310791 -5.0206298828125 9.998701095581055
    node 14 -10.43019962310791 -1.486672282218933 9.998701095581055
    node 15 -13.9641580581665 -5.0206298828125 9.998701095581055
    node 16 -13.9641580581665 -1.486672282218933 9.998701095581055
    node 17 -10.43019962310791 -8.554587364196777 9.998701095581055
    node 18 -13.9641580581665 -8.554587364196777 9.998701095581055
    node 19 -6.896242141723633 -5.0206298828125 4.999350547790527
    node 20 -6.896242141723633 -1.486672282218933 4.999350547790527
    node 21 -6.896242141723633 -1.486672282218933 0.0
    node 22 -6.896242141723633 -5.0206298828125 0.0
    node 23 -6.896242141723633 -8.554587364196777 4.999350547790527
    node 24 -6.896242141723633 -8.554587364196777 0.0
    node 25 -6.896242141723633 -5.0206298828125 9.998701095581055
    node 26 -6.896242141723633 -1.486672282218933 9.998701095581055
    node 27 -6.896242141723633 -8.554587364196777 9.998701095581055
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 0 } {
    node 40 -6.896242141723633 -6.787608623504639 4.999350547790527
    node 41 -10.43019962310791 -6.787608623504639 9.998701095581055
    node 43 -10.43019962310791 -6.787608623504639 0.0
    node 44 -10.43019962310791 -3.253651082515717 9.998701095581055
    node 45 -10.43019962310791 -8.554587364196777 2.499675273895264
    node 46 -13.9641580581665 -6.787608623504639 4.999350547790527
    node 55 -6.896242141723633 -3.253651082515717 9.998701095581055
    node 56 -6.896242141723633 -3.253651082515717 4.999350547790527
    node 57 -10.43019962310791 -1.486672282218933 7.499025821685791
    node 59 -13.9641580581665 -3.253651082515717 9.998701095581055
    node 60 -13.9641580581665 -1.486672282218933 7.499025821685791
    node 69 -6.896242141723633 -6.787608623504639 9.998701095581055
    node 70 -10.43019962310791 -8.554587364196777 7.499025821685791
    node 71 -13.9641580581665 -6.787608623504639 9.998701095581055
    node 72 -6.896242141723633 -1.486672282218933 2.499675273895264
    node 73 -13.9641580581665 -8.554587364196777 7.499025821685791
    node 74 -12.19717884063721 -8.554587364196777 9.998701095581055
    node 80 -6.896242141723633 -3.253651082515717 0.0
    node 81 -6.896242141723633 -5.0206298828125 2.499675273895264
    node 83 -8.663220882415771 -1.486672282218933 4.999350547790527
    node 92 -6.896242141723633 -6.787608623504639 0.0
    node 93 -6.896242141723633 -8.554587364196777 7.499025821685791
    node 94 -6.896242141723633 -8.554587364196777 2.499675273895264
    node 95 -8.663220882415771 -8.554587364196777 4.999350547790527
    node 96 -6.896242141723633 -1.486672282218933 7.499025821685791
    node 97 -8.663220882415771 -8.554587364196777 0.0
    node 103 -6.896242141723633 -5.0206298828125 7.499025821685791
    node 104 -8.663220882415771 -5.0206298828125 9.998701095581055
    node 105 -8.663220882415771 -1.486672282218933 9.998701095581055
    node 106 -8.663220882415771 -8.554587364196777 9.998701095581055
    node 116 -10.43019962310791 -1.486672282218933 2.499675273895264
    node 117 -10.43019962310791 -3.253651082515717 0.0
    node 119 -13.9641580581665 -3.253651082515717 4.999350547790527
    node 120 -13.9641580581665 -1.486672282218933 2.499675273895264
    node 121 -13.9641580581665 -3.253651082515717 0.0
    node 122 -13.9641580581665 -5.0206298828125 2.499675273895264
    node 124 -12.19717884063721 -1.486672282218933 4.999350547790527
    node 125 -12.19717884063721 -1.486672282218933 0.0
    node 126 -12.19717884063721 -5.0206298828125 0.0
    node 127 -13.9641580581665 -6.787608623504639 0.0
    node 128 -13.9641580581665 -8.554587364196777 2.499675273895264
    node 129 -12.19717884063721 -8.554587364196777 4.999350547790527
    node 130 -12.19717884063721 -8.554587364196777 0.0
    node 131 -13.9641580581665 -5.0206298828125 7.499025821685791
    node 132 -12.19717884063721 -5.0206298828125 9.998701095581055
    node 133 -12.19717884063721 -1.486672282218933 9.998701095581055
    node 134 -8.663220882415771 -1.486672282218933 0.0
    node 135 -8.663220882415771 -5.0206298828125 0.0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 0 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 0 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 0 1
}
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    remove sp 11 4
    fix 11 1 0 0 1
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 0 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 0 1
}
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    remove sp 11 4
    fix 11 1 0 0 1
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    fix 12 1 0 0 1
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    remove sp 12 4
    fix 12 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 0 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 0 1
}
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    remove sp 11 4
    fix 11 1 0 0 1
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    fix 12 1 0 0 1
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    remove sp 12 4
    fix 12 1 0 0 1
}
if { $pid == 1 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    fix 15 1 0 0 1
}
if { $pid == 0 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    remove sp 15 4
    fix 15 1 0 0 1
}
if { $pid == 2 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    fix 15 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 0 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 0 1
}
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    remove sp 11 4
    fix 11 1 0 0 1
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    fix 12 1 0 0 1
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    remove sp 12 4
    fix 12 1 0 0 1
}
if { $pid == 1 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    fix 15 1 0 0 1
}
if { $pid == 0 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    remove sp 15 4
    fix 15 1 0 0 1
}
if { $pid == 2 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    fix 15 1 0 0 1
}
if { $pid == 1 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
    fix 16 1 0 0 1
}
if { $pid == 0 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
    remove sp 16 4
    fix 16 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    remove sp 5 4
    fix 5 1 0 0 1
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
    fix 5 1 0 0 1
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 0 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 0 0 1
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 0 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 0 0 1
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 0 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 0 1
}
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    remove sp 11 4
    fix 11 1 0 0 1
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 0 0 1
}
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    fix 12 1 0 0 1
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    remove sp 12 4
    fix 12 1 0 0 1
}
if { $pid == 1 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    fix 15 1 0 0 1
}
if { $pid == 0 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    remove sp 15 4
    fix 15 1 0 0 1
}
if { $pid == 2 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
    fix 15 1 0 0 1
}
if { $pid == 1 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
    fix 16 1 0 0 1
}
if { $pid == 0 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
    remove sp 16 4
    fix 16 1 0 0 1
}
if { $pid == 2 } {
    remove sp 18 1
    remove sp 18 2
    remove sp 18 3
    fix 18 1 0 0 1
}
if { $pid == 0 } {
    remove sp 18 1
    remove sp 18 2
    remove sp 18 3
    remove sp 18 4
    fix 18 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 1 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 0 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 1 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 0 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 1 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 0
}
if { $pid == 0 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 1 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 0 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 1 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 0
}
if { $pid == 0 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 0
}
if { $pid == 1 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
    fix 128 1 0 0
}
if { $pid == 0 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
    fix 128 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
    fix 46 1 0 0
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 0 0
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 0 0
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
    fix 119 1 0 0
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 0 0
}
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 0
}
if { $pid == 1 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 0 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
    fix 122 1 0 0
}
if { $pid == 1 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 0
}
if { $pid == 0 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 0
}
if { $pid == 1 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
    fix 128 1 0 0
}
if { $pid == 0 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
    fix 128 1 0 0
}
if { $pid == 1 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
    fix 131 1 0 0
}
if { $pid == 0 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
    fix 131 1 0 0
}
if { $pid == 2 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
    fix 131 1 0 0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
    fix 19 1 0 0 1
}
if { $pid == 0 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
    remove sp 19 4
    fix 19 1 0 0 1
}
if { $pid == 3 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
    fix 19 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
    fix 20 1 0 0 1
}
if { $pid == 0 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
    remove sp 20 4
    fix 20 1 0 0 1
}
if { $pid == 3 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
    fix 20 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
    fix 21 1 0 0 1
}
if { $pid == 0 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
    remove sp 21 4
    fix 21 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 22 1
    remove sp 22 2
    remove sp 22 3
    fix 22 1 0 0 1
}
if { $pid == 0 } {
    remove sp 22 1
    remove sp 22 2
    remove sp 22 3
    remove sp 22 4
    fix 22 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
    fix 23 1 0 0 1
}
if { $pid == 0 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
    remove sp 23 4
    fix 23 1 0 0 1
}
if { $pid == 3 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
    fix 23 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
    fix 24 1 0 0 1
}
if { $pid == 0 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
    remove sp 24 4
    fix 24 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 3 } {
    remove sp 25 1
    remove sp 25 2
    remove sp 25 3
    fix 25 1 0 0 1
}
if { $pid == 0 } {
    remove sp 25 1
    remove sp 25 2
    remove sp 25 3
    remove sp 25 4
    fix 25 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 3 } {
    remove sp 26 1
    remove sp 26 2
    remove sp 26 3
    fix 26 1 0 0 1
}
if { $pid == 0 } {
    remove sp 26 1
    remove sp 26 2
    remove sp 26 3
    remove sp 26 4
    fix 26 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 3 } {
    remove sp 27 1
    remove sp 27 2
    remove sp 27 3
    fix 27 1 0 0 1
}
if { $pid == 0 } {
    remove sp 27 1
    remove sp 27 2
    remove sp 27 3
    remove sp 27 4
    fix 27 1 0 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
    fix 40 1 0 0
}
if { $pid == 0 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
    fix 40 1 0 0
}
if { $pid == 3 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
    fix 40 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 55 1
    remove sp 55 2
    remove sp 55 3
    fix 55 1 0 0
}
if { $pid == 0 } {
    remove sp 55 1
    remove sp 55 2
    remove sp 55 3
    fix 55 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
    fix 56 1 0 0
}
if { $pid == 0 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
    fix 56 1 0 0
}
if { $pid == 3 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
    fix 56 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 69 1
    remove sp 69 2
    remove sp 69 3
    fix 69 1 0 0
}
if { $pid == 0 } {
    remove sp 69 1
    remove sp 69 2
    remove sp 69 3
    fix 69 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 72 1
    remove sp 72 2
    remove sp 72 3
    fix 72 1 0 0
}
if { $pid == 0 } {
    remove sp 72 1
    remove sp 72 2
    remove sp 72 3
    fix 72 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 80 1
    remove sp 80 2
    remove sp 80 3
    fix 80 1 0 0
}
if { $pid == 0 } {
    remove sp 80 1
    remove sp 80 2
    remove sp 80 3
    fix 80 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 81 1
    remove sp 81 2
    remove sp 81 3
    fix 81 1 0 0
}
if { $pid == 0 } {
    remove sp 81 1
    remove sp 81 2
    remove sp 81 3
    fix 81 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 92 1
    remove sp 92 2
    remove sp 92 3
    fix 92 1 0 0
}
if { $pid == 0 } {
    remove sp 92 1
    remove sp 92 2
    remove sp 92 3
    fix 92 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 93 1
    remove sp 93 2
    remove sp 93 3
    fix 93 1 0 0
}
if { $pid == 0 } {
    remove sp 93 1
    remove sp 93 2
    remove sp 93 3
    fix 93 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 94 1
    remove sp 94 2
    remove sp 94 3
    fix 94 1 0 0
}
if { $pid == 0 } {
    remove sp 94 1
    remove sp 94 2
    remove sp 94 3
    fix 94 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 96 1
    remove sp 96 2
    remove sp 96 3
    fix 96 1 0 0
}
if { $pid == 0 } {
    remove sp 96 1
    remove sp 96 2
    remove sp 96 3
    fix 96 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 103 1
    remove sp 103 2
    remove sp 103 3
    fix 103 1 0 0
}
if { $pid == 0 } {
    remove sp 103 1
    remove sp 103 2
    remove sp 103 3
    fix 103 1 0 0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 9 1
    remove sp 9 2
    remove sp 9 3
    fix 9 0 1 0 1
}
if { $pid == 0 } {
    remove sp 9 1
    remove sp 9 2
    remove sp 9 3
    remove sp 9 4
    fix 9 0 1 0 1
}
if { $pid == 2 } {
    remove sp 9 1
    remove sp 9 2
    remove sp 9 3
    fix 9 0 1 0 1
}
if { $pid == 3 } {
    remove sp 9 1
    remove sp 9 2
    remove sp 9 3
    fix 9 0 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 10 1
    remove sp 10 2
    remove sp 10 3
    fix 10 0 1 0 1
}
if { $pid == 0 } {
    remove sp 10 1
    remove sp 10 2
    remove sp 10 3
    remove sp 10 4
    fix 10 0 1 0 1
}
if { $pid == 2 } {
    remove sp 10 1
    remove sp 10 2
    remove sp 10 3
    fix 10 0 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 1 0 1
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    remove sp 11 4
    fix 11 1 1 0 1
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
    fix 11 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    fix 12 1 1 0 1
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    remove sp 12 4
    fix 12 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 17 1
    remove sp 17 2
    remove sp 17 3
    fix 17 0 1 0 1
}
if { $pid == 0 } {
    remove sp 17 1
    remove sp 17 2
    remove sp 17 3
    remove sp 17 4
    fix 17 0 1 0 1
}
if { $pid == 3 } {
    remove sp 17 1
    remove sp 17 2
    remove sp 17 3
    fix 17 0 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 18 1
    remove sp 18 2
    remove sp 18 3
    fix 18 1 1 0 1
}
if { $pid == 0 } {
    remove sp 18 1
    remove sp 18 2
    remove sp 18 3
    remove sp 18 4
    fix 18 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
    fix 23 1 1 0 1
}
if { $pid == 0 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
    remove sp 23 4
    fix 23 1 1 0 1
}
if { $pid == 3 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
    fix 23 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
    fix 24 1 1 0 1
}
if { $pid == 0 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
    remove sp 24 4
    fix 24 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 3 } {
    remove sp 27 1
    remove sp 27 2
    remove sp 27 3
    fix 27 1 1 0 1
}
if { $pid == 0 } {
    remove sp 27 1
    remove sp 27 2
    remove sp 27 3
    remove sp 27 4
    fix 27 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 45 1
    remove sp 45 2
    remove sp 45 3
    fix 45 0 1 0
}
if { $pid == 0 } {
    remove sp 45 1
    remove sp 45 2
    remove sp 45 3
    fix 45 0 1 0
}
if { $pid == 2 } {
    remove sp 45 1
    remove sp 45 2
    remove sp 45 3
    fix 45 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 70 1
    remove sp 70 2
    remove sp 70 3
    fix 70 0 1 0
}
if { $pid == 0 } {
    remove sp 70 1
    remove sp 70 2
    remove sp 70 3
    fix 70 0 1 0
}
if { $pid == 3 } {
    remove sp 70 1
    remove sp 70 2
    remove sp 70 3
    fix 70 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 1 0
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
    fix 73 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 74 1
    remove sp 74 2
    remove sp 74 3
    fix 74 0 1 0
}
if { $pid == 0 } {
    remove sp 74 1
    remove sp 74 2
    remove sp 74 3
    fix 74 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 93 1
    remove sp 93 2
    remove sp 93 3
    fix 93 1 1 0
}
if { $pid == 0 } {
    remove sp 93 1
    remove sp 93 2
    remove sp 93 3
    fix 93 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 94 1
    remove sp 94 2
    remove sp 94 3
    fix 94 1 1 0
}
if { $pid == 0 } {
    remove sp 94 1
    remove sp 94 2
    remove sp 94 3
    fix 94 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 95 1
    remove sp 95 2
    remove sp 95 3
    fix 95 0 1 0
}
if { $pid == 0 } {
    remove sp 95 1
    remove sp 95 2
    remove sp 95 3
    fix 95 0 1 0
}
if { $pid == 3 } {
    remove sp 95 1
    remove sp 95 2
    remove sp 95 3
    fix 95 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 97 1
    remove sp 97 2
    remove sp 97 3
    fix 97 0 1 0
}
if { $pid == 0 } {
    remove sp 97 1
    remove sp 97 2
    remove sp 97 3
    fix 97 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 106 1
    remove sp 106 2
    remove sp 106 3
    fix 106 0 1 0
}
if { $pid == 0 } {
    remove sp 106 1
    remove sp 106 2
    remove sp 106 3
    fix 106 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
    fix 128 1 1 0
}
if { $pid == 0 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
    fix 128 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 129 1
    remove sp 129 2
    remove sp 129 3
    fix 129 0 1 0
}
if { $pid == 0 } {
    remove sp 129 1
    remove sp 129 2
    remove sp 129 3
    fix 129 0 1 0
}
if { $pid == 2 } {
    remove sp 129 1
    remove sp 129 2
    remove sp 129 3
    fix 129 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 130 1
    remove sp 130 2
    remove sp 130 3
    fix 130 0 1 0
}
if { $pid == 0 } {
    remove sp 130 1
    remove sp 130 2
    remove sp 130 3
    fix 130 0 1 0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 2 1
    remove sp 2 2
    remove sp 2 3
    fix 2 0 1 0 1
}
if { $pid == 0 } {
    remove sp 2 1
    remove sp 2 2
    remove sp 2 3
    remove sp 2 4
    fix 2 0 1 0 1
}
if { $pid == 2 } {
    remove sp 2 1
    remove sp 2 2
    remove sp 2 3
    fix 2 0 1 0 1
}
if { $pid == 3 } {
    remove sp 2 1
    remove sp 2 2
    remove sp 2 3
    fix 2 0 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 3 1
    remove sp 3 2
    remove sp 3 3
    fix 3 0 1 0 1
}
if { $pid == 0 } {
    remove sp 3 1
    remove sp 3 2
    remove sp 3 3
    remove sp 3 4
    fix 3 0 1 0 1
}
if { $pid == 2 } {
    remove sp 3 1
    remove sp 3 2
    remove sp 3 3
    fix 3 0 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    fix 6 1 1 0 1
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
    remove sp 6 4
    fix 6 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 1 0 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 14 1
    remove sp 14 2
    remove sp 14 3
    fix 14 0 1 0 1
}
if { $pid == 0 } {
    remove sp 14 1
    remove sp 14 2
    remove sp 14 3
    remove sp 14 4
    fix 14 0 1 0 1
}
if { $pid == 3 } {
    remove sp 14 1
    remove sp 14 2
    remove sp 14 3
    fix 14 0 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
    fix 16 1 1 0 1
}
if { $pid == 0 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
    remove sp 16 4
    fix 16 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
    fix 20 1 1 0 1
}
if { $pid == 0 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
    remove sp 20 4
    fix 20 1 1 0 1
}
if { $pid == 3 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
    fix 20 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
    fix 21 1 1 0 1
}
if { $pid == 0 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
    remove sp 21 4
    fix 21 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 3 } {
    remove sp 26 1
    remove sp 26 2
    remove sp 26 3
    fix 26 1 1 0 1
}
if { $pid == 0 } {
    remove sp 26 1
    remove sp 26 2
    remove sp 26 3
    remove sp 26 4
    fix 26 1 1 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 57 1
    remove sp 57 2
    remove sp 57 3
    fix 57 0 1 0
}
if { $pid == 0 } {
    remove sp 57 1
    remove sp 57 2
    remove sp 57 3
    fix 57 0 1 0
}
if { $pid == 3 } {
    remove sp 57 1
    remove sp 57 2
    remove sp 57 3
    fix 57 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 1 0
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
    fix 60 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 72 1
    remove sp 72 2
    remove sp 72 3
    fix 72 1 1 0
}
if { $pid == 0 } {
    remove sp 72 1
    remove sp 72 2
    remove sp 72 3
    fix 72 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 83 1
    remove sp 83 2
    remove sp 83 3
    fix 83 0 1 0
}
if { $pid == 0 } {
    remove sp 83 1
    remove sp 83 2
    remove sp 83 3
    fix 83 0 1 0
}
if { $pid == 3 } {
    remove sp 83 1
    remove sp 83 2
    remove sp 83 3
    fix 83 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 96 1
    remove sp 96 2
    remove sp 96 3
    fix 96 1 1 0
}
if { $pid == 0 } {
    remove sp 96 1
    remove sp 96 2
    remove sp 96 3
    fix 96 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 105 1
    remove sp 105 2
    remove sp 105 3
    fix 105 0 1 0
}
if { $pid == 0 } {
    remove sp 105 1
    remove sp 105 2
    remove sp 105 3
    fix 105 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 116 1
    remove sp 116 2
    remove sp 116 3
    fix 116 0 1 0
}
if { $pid == 0 } {
    remove sp 116 1
    remove sp 116 2
    remove sp 116 3
    fix 116 0 1 0
}
if { $pid == 2 } {
    remove sp 116 1
    remove sp 116 2
    remove sp 116 3
    fix 116 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 1 0
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
    fix 120 1 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 124 1
    remove sp 124 2
    remove sp 124 3
    fix 124 0 1 0
}
if { $pid == 0 } {
    remove sp 124 1
    remove sp 124 2
    remove sp 124 3
    fix 124 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 125 1
    remove sp 125 2
    remove sp 125 3
    fix 125 0 1 0
}
if { $pid == 0 } {
    remove sp 125 1
    remove sp 125 2
    remove sp 125 3
    fix 125 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 133 1
    remove sp 133 2
    remove sp 133 3
    fix 133 0 1 0
}
if { $pid == 0 } {
    remove sp 133 1
    remove sp 133 2
    remove sp 133 3
    fix 133 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 134 1
    remove sp 134 2
    remove sp 134 3
    fix 134 0 1 0
}
if { $pid == 0 } {
    remove sp 134 1
    remove sp 134 2
    remove sp 134 3
    fix 134 0 1 0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 3 1
    remove sp 3 2
    remove sp 3 3
    fix 3 0 1 1 1
}
if { $pid == 0 } {
    remove sp 3 1
    remove sp 3 2
    remove sp 3 3
    remove sp 3 4
    fix 3 0 1 1 1
}
if { $pid == 2 } {
    remove sp 3 1
    remove sp 3 2
    remove sp 3 3
    fix 3 0 1 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 4 1
    remove sp 4 2
    remove sp 4 3
    fix 4 0 0 1 1
}
if { $pid == 0 } {
    remove sp 4 1
    remove sp 4 2
    remove sp 4 3
    remove sp 4 4
    fix 4 0 0 1 1
}
if { $pid == 2 } {
    remove sp 4 1
    remove sp 4 2
    remove sp 4 3
    fix 4 0 0 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    fix 7 1 1 1 1
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
    remove sp 7 4
    fix 7 1 1 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    fix 8 1 0 1 1
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
    remove sp 8 4
    fix 8 1 0 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 10 1
    remove sp 10 2
    remove sp 10 3
    fix 10 0 1 1 1
}
if { $pid == 0 } {
    remove sp 10 1
    remove sp 10 2
    remove sp 10 3
    remove sp 10 4
    fix 10 0 1 1 1
}
if { $pid == 2 } {
    remove sp 10 1
    remove sp 10 2
    remove sp 10 3
    fix 10 0 1 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    fix 12 1 1 1 1
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
    remove sp 12 4
    fix 12 1 1 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
    fix 21 1 1 1 1
}
if { $pid == 0 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
    remove sp 21 4
    fix 21 1 1 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 22 1
    remove sp 22 2
    remove sp 22 3
    fix 22 1 0 1 1
}
if { $pid == 0 } {
    remove sp 22 1
    remove sp 22 2
    remove sp 22 3
    remove sp 22 4
    fix 22 1 0 1 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
    fix 24 1 1 1 1
}
if { $pid == 0 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
    remove sp 24 4
    fix 24 1 1 1 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 43 1
    remove sp 43 2
    remove sp 43 3
    fix 43 0 0 1
}
if { $pid == 0 } {
    remove sp 43 1
    remove sp 43 2
    remove sp 43 3
    fix 43 0 0 1
}
if { $pid == 2 } {
    remove sp 43 1
    remove sp 43 2
    remove sp 43 3
    fix 43 0 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 80 1
    remove sp 80 2
    remove sp 80 3
    fix 80 1 0 1
}
if { $pid == 0 } {
    remove sp 80 1
    remove sp 80 2
    remove sp 80 3
    fix 80 1 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 92 1
    remove sp 92 2
    remove sp 92 3
    fix 92 1 0 1
}
if { $pid == 0 } {
    remove sp 92 1
    remove sp 92 2
    remove sp 92 3
    fix 92 1 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 97 1
    remove sp 97 2
    remove sp 97 3
    fix 97 0 1 1
}
if { $pid == 0 } {
    remove sp 97 1
    remove sp 97 2
    remove sp 97 3
    fix 97 0 1 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 117 1
    remove sp 117 2
    remove sp 117 3
    fix 117 0 0 1
}
if { $pid == 0 } {
    remove sp 117 1
    remove sp 117 2
    remove sp 117 3
    fix 117 0 0 1
}
if { $pid == 2 } {
    remove sp 117 1
    remove sp 117 2
    remove sp 117 3
    fix 117 0 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 1
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
    fix 121 1 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 125 1
    remove sp 125 2
    remove sp 125 3
    fix 125 0 1 1
}
if { $pid == 0 } {
    remove sp 125 1
    remove sp 125 2
    remove sp 125 3
    fix 125 0 1 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 126 1
    remove sp 126 2
    remove sp 126 3
    fix 126 0 0 1
}
if { $pid == 0 } {
    remove sp 126 1
    remove sp 126 2
    remove sp 126 3
    fix 126 0 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 1
}
if { $pid == 0 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
    fix 127 1 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 130 1
    remove sp 130 2
    remove sp 130 3
    fix 130 0 1 1
}
if { $pid == 0 } {
    remove sp 130 1
    remove sp 130 2
    remove sp 130 3
    fix 130 0 1 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 134 1
    remove sp 134 2
    remove sp 134 3
    fix 134 0 1 1
}
if { $pid == 0 } {
    remove sp 134 1
    remove sp 134 2
    remove sp 134 3
    fix 134 0 1 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 135 1
    remove sp 135 2
    remove sp 135 3
    fix 135 0 0 1
}
if { $pid == 0 } {
    remove sp 135 1
    remove sp 135 2
    remove sp 135 3
    fix 135 0 0 1
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 13 1
    remove sp 13 2
    remove sp 13 3
    fix 13 0 0 0 1
}
if { $pid == 0 } {
    remove sp 13 1
    remove sp 13 2
    remove sp 13 3
    remove sp 13 4
    fix 13 0 0 0 1
}
if { $pid == 2 } {
    remove sp 13 1
    remove sp 13 2
    remove sp 13 3
    fix 13 0 0 0 1
}
if { $pid == 3 } {
    remove sp 13 1
    remove sp 13 2
    remove sp 13 3
    fix 13 0 0 0 1
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 41 1
    remove sp 41 2
    remove sp 41 3
    fix 41 0 0 0
}
if { $pid == 0 } {
    remove sp 41 1
    remove sp 41 2
    remove sp 41 3
    fix 41 0 0 0
}
if { $pid == 3 } {
    remove sp 41 1
    remove sp 41 2
    remove sp 41 3
    fix 41 0 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 44 1
    remove sp 44 2
    remove sp 44 3
    fix 44 0 0 0
}
if { $pid == 0 } {
    remove sp 44 1
    remove sp 44 2
    remove sp 44 3
    fix 44 0 0 0
}
if { $pid == 3 } {
    remove sp 44 1
    remove sp 44 2
    remove sp 44 3
    fix 44 0 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 55 1
    remove sp 55 2
    remove sp 55 3
    fix 55 1 0 0
}
if { $pid == 0 } {
    remove sp 55 1
    remove sp 55 2
    remove sp 55 3
    fix 55 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
    fix 59 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 69 1
    remove sp 69 2
    remove sp 69 3
    fix 69 1 0 0
}
if { $pid == 0 } {
    remove sp 69 1
    remove sp 69 2
    remove sp 69 3
    fix 69 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
    fix 71 1 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 74 1
    remove sp 74 2
    remove sp 74 3
    fix 74 0 1 0
}
if { $pid == 0 } {
    remove sp 74 1
    remove sp 74 2
    remove sp 74 3
    fix 74 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 104 1
    remove sp 104 2
    remove sp 104 3
    fix 104 0 0 0
}
if { $pid == 0 } {
    remove sp 104 1
    remove sp 104 2
    remove sp 104 3
    fix 104 0 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 105 1
    remove sp 105 2
    remove sp 105 3
    fix 105 0 1 0
}
if { $pid == 0 } {
    remove sp 105 1
    remove sp 105 2
    remove sp 105 3
    fix 105 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 3 } {
    remove sp 106 1
    remove sp 106 2
    remove sp 106 3
    fix 106 0 1 0
}
if { $pid == 0 } {
    remove sp 106 1
    remove sp 106 2
    remove sp 106 3
    fix 106 0 1 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 132 1
    remove sp 132 2
    remove sp 132 3
    fix 132 0 0 0
}
if { $pid == 0 } {
    remove sp 132 1
    remove sp 132 2
    remove sp 132 3
    fix 132 0 0 0
}
if { $pid == 2 } {
    remove sp 132 1
    remove sp 132 2
    remove sp 132 3
    fix 132 0 0 0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 133 1
    remove sp 133 2
    remove sp 133 3
    fix 133 0 1 0
}
if { $pid == 0 } {
    remove sp 133 1
    remove sp 133 2
    remove sp 133 3
    fix 133 0 1 0
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    element 20_8_BrickUP 1 8 4 3 7 5 1 2 6 126 117 125 121 123 115 124 119 122 118 116 120 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 1 } {
    element 20_8_BrickUP 2 12 10 4 8 11 9 1 5 130 43 126 127 129 42 123 46 128 45 118 122 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 1 } {
    element 20_8_BrickUP 3 5 1 2 6 15 13 14 16 123 115 124 119 132 44 133 59 131 58 57 60 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 2 } {
    element 20_8_BrickUP 4 11 9 1 5 18 17 13 15 129 42 123 46 74 41 132 71 73 70 58 131 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 2 } {
    element 20_8_BrickUP 5 4 22 21 3 1 19 20 2 135 80 134 117 82 56 83 115 118 81 72 116 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 2 } {
    element 20_8_BrickUP 6 10 24 22 4 9 23 19 1 97 92 135 43 95 40 82 42 45 94 81 118 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 3 } {
    element 20_8_BrickUP 7 1 19 20 2 13 25 26 14 82 56 83 115 104 55 105 44 58 103 96 57 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
if { $pid == 3 } {
    element 20_8_BrickUP 8 9 23 19 1 17 27 25 13 95 40 82 42 106 69 104 41 70 93 103 58 1  2.2e6 1 1.0 1.0 1.0 0.0 0.0 -20.0
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    node 136 -10.4 -5.02 0.0
    node 137 -10.4 -5.02 0.0
    fix 137 1 1 1
    fix 136 0 1 1
    equalDOF 4 136 1
    uniaxialMaterial Viscous 2 31501.260000000002 1
    set dir 1
    element zeroLength  9 137 136 -mat 2 -dir $dir
}
if { $pid == 2 } {
    node 136 -10.4 -5.02 0.0
    node 137 -10.4 -5.02 0.0
    fix 137 1 1 1
    fix 136 0 1 1
    equalDOF 4 136 1
    uniaxialMaterial Viscous 2 31501.260000000002 1
    set dir 1
    element zeroLength  9 137 136 -mat 2 -dir $dir
}

set motionDT 0.002
set motionSteps  20001
set nSteps 20001
set dT 0.002
puts "ANALISI STATICA START"
model BasicBuilder -ndm 3 -ndf 4
model BasicBuilder -ndm 3 -ndf 4
updateMaterialStage -material 1 -stage 0
updateMaterialStage -material 2 -stage 0
constraints Transformation
test NormDispIncr 1e-3 100 1
algorithm ModifiedNewton
numberer ParallelPlain
system Mumps
integrator Newmark 0.5 0.25
analysis Transient
analyze 10 1
puts "ANALISI STATICA END"

model BasicBuilder -ndm 3 -ndf 4
updateMaterialStage -material 1 -stage 1
updateMaterialStage -material 2 -stage 1
domainChange
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 1 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
}
if { $pid == 2 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
}
if { $pid == 0 } {
    remove sp 5 1
    remove sp 5 2
    remove sp 5 3
}
if { $pid == 1 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
}
if { $pid == 0 } {
    remove sp 6 1
    remove sp 6 2
    remove sp 6 3
}
if { $pid == 1 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
}
if { $pid == 0 } {
    remove sp 7 1
    remove sp 7 2
    remove sp 7 3
}
if { $pid == 1 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
}
if { $pid == 0 } {
    remove sp 8 1
    remove sp 8 2
    remove sp 8 3
}
if { $pid == 1 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
}
if { $pid == 2 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
}
if { $pid == 0 } {
    remove sp 11 1
    remove sp 11 2
    remove sp 11 3
}
if { $pid == 1 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
}
if { $pid == 0 } {
    remove sp 12 1
    remove sp 12 2
    remove sp 12 3
}
if { $pid == 1 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
}
if { $pid == 0 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
}
if { $pid == 2 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
}
if { $pid == 0 } {
    remove sp 15 1
    remove sp 15 2
    remove sp 15 3
}
if { $pid == 1 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
}
if { $pid == 0 } {
    remove sp 16 1
    remove sp 16 2
    remove sp 16 3
}
if { $pid == 2 } {
    remove sp 18 1
    remove sp 18 2
    remove sp 18 3
}
if { $pid == 0 } {
    remove sp 18 1
    remove sp 18 2
    remove sp 18 3
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 1 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
}
if { $pid == 2 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
}
if { $pid == 0 } {
    remove sp 46 1
    remove sp 46 2
    remove sp 46 3
}
if { $pid == 1 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
}
if { $pid == 0 } {
    remove sp 59 1
    remove sp 59 2
    remove sp 59 3
}
if { $pid == 1 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
}
if { $pid == 0 } {
    remove sp 60 1
    remove sp 60 2
    remove sp 60 3
}
if { $pid == 2 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
}
if { $pid == 0 } {
    remove sp 71 1
    remove sp 71 2
    remove sp 71 3
}
if { $pid == 2 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
}
if { $pid == 0 } {
    remove sp 73 1
    remove sp 73 2
    remove sp 73 3
}
if { $pid == 1 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
}
if { $pid == 0 } {
    remove sp 119 1
    remove sp 119 2
    remove sp 119 3
}
if { $pid == 1 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
}
if { $pid == 0 } {
    remove sp 120 1
    remove sp 120 2
    remove sp 120 3
}
if { $pid == 1 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
}
if { $pid == 0 } {
    remove sp 121 1
    remove sp 121 2
    remove sp 121 3
}
if { $pid == 1 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
}
if { $pid == 0 } {
    remove sp 122 1
    remove sp 122 2
    remove sp 122 3
}
if { $pid == 1 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
}
if { $pid == 0 } {
    remove sp 127 1
    remove sp 127 2
    remove sp 127 3
}
if { $pid == 1 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
}
if { $pid == 0 } {
    remove sp 128 1
    remove sp 128 2
    remove sp 128 3
}
if { $pid == 1 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
}
if { $pid == 0 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
}
if { $pid == 2 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
}
if { $pid == 0 } {
    remove sp 131 1
    remove sp 131 2
    remove sp 131 3
}
model BasicBuilder -ndm 3 -ndf 4
if { $pid == 2 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
}
if { $pid == 0 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
}
if { $pid == 3 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
}
if { $pid == 0 } {
    remove sp 19 1
    remove sp 19 2
    remove sp 19 3
}
if { $pid == 2 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
}
if { $pid == 0 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
}
if { $pid == 3 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
}
if { $pid == 0 } {
    remove sp 20 1
    remove sp 20 2
    remove sp 20 3
}
if { $pid == 2 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
}
if { $pid == 0 } {
    remove sp 21 1
    remove sp 21 2
    remove sp 21 3
}
if { $pid == 2 } {
    remove sp 22 1
    remove sp 22 2
    remove sp 22 3
}
if { $pid == 0 } {
    remove sp 22 1
    remove sp 22 2
    remove sp 22 3
}
if { $pid == 2 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
}
if { $pid == 0 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
}
if { $pid == 3 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
}
if { $pid == 0 } {
    remove sp 23 1
    remove sp 23 2
    remove sp 23 3
}
if { $pid == 2 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
}
if { $pid == 0 } {
    remove sp 24 1
    remove sp 24 2
    remove sp 24 3
}
if { $pid == 3 } {
    remove sp 25 1
    remove sp 25 2
    remove sp 25 3
}
if { $pid == 0 } {
    remove sp 25 1
    remove sp 25 2
    remove sp 25 3
}
if { $pid == 3 } {
    remove sp 26 1
    remove sp 26 2
    remove sp 26 3
}
if { $pid == 0 } {
    remove sp 26 1
    remove sp 26 2
    remove sp 26 3
}
if { $pid == 3 } {
    remove sp 27 1
    remove sp 27 2
    remove sp 27 3
}
if { $pid == 0 } {
    remove sp 27 1
    remove sp 27 2
    remove sp 27 3
}
model BasicBuilder -ndm 3 -ndf 3
if { $pid == 2 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
}
if { $pid == 0 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
}
if { $pid == 3 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
}
if { $pid == 0 } {
    remove sp 40 1
    remove sp 40 2
    remove sp 40 3
}
if { $pid == 3 } {
    remove sp 55 1
    remove sp 55 2
    remove sp 55 3
}
if { $pid == 0 } {
    remove sp 55 1
    remove sp 55 2
    remove sp 55 3
}
if { $pid == 2 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
}
if { $pid == 0 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
}
if { $pid == 3 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
}
if { $pid == 0 } {
    remove sp 56 1
    remove sp 56 2
    remove sp 56 3
}
if { $pid == 3 } {
    remove sp 69 1
    remove sp 69 2
    remove sp 69 3
}
if { $pid == 0 } {
    remove sp 69 1
    remove sp 69 2
    remove sp 69 3
}
if { $pid == 2 } {
    remove sp 72 1
    remove sp 72 2
    remove sp 72 3
}
if { $pid == 0 } {
    remove sp 72 1
    remove sp 72 2
    remove sp 72 3
}
if { $pid == 2 } {
    remove sp 80 1
    remove sp 80 2
    remove sp 80 3
}
if { $pid == 0 } {
    remove sp 80 1
    remove sp 80 2
    remove sp 80 3
}
if { $pid == 2 } {
    remove sp 81 1
    remove sp 81 2
    remove sp 81 3
}
if { $pid == 0 } {
    remove sp 81 1
    remove sp 81 2
    remove sp 81 3
}
if { $pid == 2 } {
    remove sp 92 1
    remove sp 92 2
    remove sp 92 3
}
if { $pid == 0 } {
    remove sp 92 1
    remove sp 92 2
    remove sp 92 3
}
if { $pid == 3 } {
    remove sp 93 1
    remove sp 93 2
    remove sp 93 3
}
if { $pid == 0 } {
    remove sp 93 1
    remove sp 93 2
    remove sp 93 3
}
if { $pid == 2 } {
    remove sp 94 1
    remove sp 94 2
    remove sp 94 3
}
if { $pid == 0 } {
    remove sp 94 1
    remove sp 94 2
    remove sp 94 3
}
if { $pid == 3 } {
    remove sp 96 1
    remove sp 96 2
    remove sp 96 3
}
if { $pid == 0 } {
    remove sp 96 1
    remove sp 96 2
    remove sp 96 3
}
if { $pid == 3 } {
    remove sp 103 1
    remove sp 103 2
    remove sp 103 3
}
if { $pid == 0 } {
    remove sp 103 1
    remove sp 103 2
    remove sp 103 3
}
if { $pid == 0 } {
    equalDOF 5 19 1 2
}
if { $pid == 0 } {
    equalDOF 5 20 1 2
}
if { $pid == 0 } {
    equalDOF 5 23 1 2
}
if { $pid == 0 } {
    equalDOF 6 19 1 2
}
if { $pid == 0 } {
    equalDOF 6 20 1 2
}
if { $pid == 0 } {
    equalDOF 6 23 1 2
}
if { $pid == 0 } {
    equalDOF 7 21 1 2
}
if { $pid == 0 } {
    equalDOF 7 22 1 2
}
if { $pid == 0 } {
    equalDOF 7 24 1 2
}
if { $pid == 0 } {
    equalDOF 8 21 1 2
}
if { $pid == 0 } {
    equalDOF 8 22 1 2
}
if { $pid == 0 } {
    equalDOF 8 24 1 2
}
if { $pid == 0 } {
    equalDOF 11 19 1 2
}
if { $pid == 0 } {
    equalDOF 11 20 1 2
}
if { $pid == 0 } {
    equalDOF 11 23 1 2
}
if { $pid == 0 } {
    equalDOF 12 21 1 2
}
if { $pid == 0 } {
    equalDOF 12 22 1 2
}
if { $pid == 0 } {
    equalDOF 12 24 1 2
}
if { $pid == 0 } {
    equalDOF 15 25 1 2
}
if { $pid == 0 } {
    equalDOF 15 26 1 2
}
if { $pid == 0 } {
    equalDOF 15 27 1 2
}
if { $pid == 0 } {
    equalDOF 16 25 1 2
}
if { $pid == 0 } {
    equalDOF 16 26 1 2
}
if { $pid == 0 } {
    equalDOF 16 27 1 2
}
if { $pid == 0 } {
    equalDOF 18 25 1 2
}
if { $pid == 0 } {
    equalDOF 18 26 1 2
}
if { $pid == 0 } {
    equalDOF 18 27 1 2
}
if { $pid == 0 } {
    equalDOF 46 40 1 2
}
if { $pid == 0 } {
    equalDOF 46 56 1 2
}
if { $pid == 0 } {
    equalDOF 59 55 1 2
}
if { $pid == 0 } {
    equalDOF 59 69 1 2
}
if { $pid == 0 } {
    equalDOF 60 93 1 2
}
if { $pid == 0 } {
    equalDOF 60 96 1 2
}
if { $pid == 0 } {
    equalDOF 60 103 1 2
}
if { $pid == 0 } {
    equalDOF 71 55 1 2
}
if { $pid == 0 } {
    equalDOF 71 69 1 2
}
if { $pid == 0 } {
    equalDOF 73 93 1 2
}
if { $pid == 0 } {
    equalDOF 73 96 1 2
}
if { $pid == 0 } {
    equalDOF 73 103 1 2
}
if { $pid == 0 } {
    equalDOF 119 40 1 2
}
if { $pid == 0 } {
    equalDOF 119 56 1 2
}
if { $pid == 0 } {
    equalDOF 120 72 1 2
}
if { $pid == 0 } {
    equalDOF 120 81 1 2
}
if { $pid == 0 } {
    equalDOF 120 94 1 2
}
if { $pid == 0 } {
    equalDOF 121 80 1 2
}
if { $pid == 0 } {
    equalDOF 121 92 1 2
}
if { $pid == 0 } {
    equalDOF 122 72 1 2
}
if { $pid == 0 } {
    equalDOF 122 81 1 2
}
if { $pid == 0 } {
    equalDOF 122 94 1 2
}
if { $pid == 0 } {
    equalDOF 127 80 1 2
}
if { $pid == 0 } {
    equalDOF 127 92 1 2
}
if { $pid == 0 } {
    equalDOF 128 72 1 2
}
if { $pid == 0 } {
    equalDOF 128 81 1 2
}
if { $pid == 0 } {
    equalDOF 128 94 1 2
}
if { $pid == 0 } {
    equalDOF 131 93 1 2
}
if { $pid == 0 } {
    equalDOF 131 96 1 2
}
if { $pid == 0 } {
    equalDOF 131 103 1 2
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 3 1
equalDOF 4 3 2
equalDOF 4 3 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 7 1
equalDOF 4 7 2
equalDOF 4 7 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 8 1
equalDOF 4 8 2
equalDOF 4 8 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 10 1
equalDOF 4 10 2
equalDOF 4 10 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 12 1
equalDOF 4 12 2
equalDOF 4 12 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 21 1
equalDOF 4 21 2
equalDOF 4 21 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 22 1
equalDOF 4 22 2
equalDOF 4 22 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 24 1
equalDOF 4 24 2
equalDOF 4 24 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 43 1
equalDOF 4 43 2
equalDOF 4 43 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 80 1
equalDOF 4 80 2
equalDOF 4 80 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 92 1
equalDOF 4 92 2
equalDOF 4 92 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 97 1
equalDOF 4 97 2
equalDOF 4 97 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 117 1
equalDOF 4 117 2
equalDOF 4 117 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 121 1
equalDOF 4 121 2
equalDOF 4 121 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 125 1
equalDOF 4 125 2
equalDOF 4 125 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 126 1
equalDOF 4 126 2
equalDOF 4 126 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 127 1
equalDOF 4 127 2
equalDOF 4 127 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 130 1
equalDOF 4 130 2
equalDOF 4 130 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 134 1
equalDOF 4 134 2
equalDOF 4 134 3
}
if { $pid == 0 } {
model BasicBuilder -ndm 3 -ndf 3
equalDOF 4 135 1
equalDOF 4 135 2
equalDOF 4 135 3
}
setTime 0.0
wipeAnalysis
remove recorders
set recDT $motionDT
set velocityFile veloma2000.out
set timeSeries "Path 2 -dt 0.002 -filePath $velocityFile -factor 6300252.0"
pattern Plain 10 $timeSeries {
if { $pid == 0} {
    load 4 0.5 0.0 0.0 0.0
}}
recorder mpco "cubotto.part-$pid.mpco" -T dt 0.002 -N "displacement" "velocity" "acceleration" "pressure" -E "material.stress" "material.strain"

puts "ANALISI DINAMICA START"
constraints Penalty 1.0E16 1.0E16
test NormDispIncr 1e-3 100 1
algorithm KrylovNewton -iterate current
numberer ParallelRCM
system Mumps -ICNTL14 200
integrator Newmark 0.5 0.25
rayleigh 0.09558 0.000792 0.0 0.0
analysis Transient
analyze 1000 0.002

puts "Finished with dynamic analysis..."
wipe
