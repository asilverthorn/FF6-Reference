import struct

hex = "E9E8E8FFE8E9E8FFE8E8E9FFBCFF42FFFFFFFFFFB3FFB3F141ADACFF30FFFFFFE9FFE8FF9FFFFFFFFFFFFFFF6EFFE8FFBDFFFFFF14FFFFFFE9FFF4FFE9FFF1F8F5FFFFF1E8E8FFFFE8F2FFFFE8E8E8FFC7FFFFFF54E8E9FF62FFFFFFE8E8E8FFE9FFE8FFE8E8E8FFE9E8E9FFE9E8E9FFE9F0FFFF8DFFE9FFFFFFFFFFD2FF8FFFBAFFEAFFFFF2FFFF0201E9FFF5F1FFFF21EAFFFFC8FFFFFFCAFFCEFF9BFF24FFE8E8FFFFE9F3E9FFF0E9F0FFF0FFFFFFFFE9FDFFAAFFFFFFE8E8FFFFF2F2E9FFFFE8F6FF56FFFFFFF5E8FFFFA0FFFFFF83FFFFFFFBFFFCFFE8F2FFFFFFFFFFFFE9E8F3FF54E8E8FFE9FFF0FF43E9FFFF12FFF4FFF6E8FFFFF5FFFFFFEE89F5F5FFFFFFFFFFE8FFFFE9E8FFE9FFEBFFFFEAFF7272A7FFFFFFE8E8E8FFF9E8FFFFB3FFF1FFFFF8FFFFC3FFFFFFFFE8FFFFF4FFF4FFE8E8E8FFBFB0B7FFE9E8E9FFD7FFFFFFF2FFFFFF04E9FFFFC4FFFFFFFFFFE5FFEEE8FFFFFFFAF9FFE9FFFFFF92EBFFFFE8FFEAFFE8E8E8FFF5FFFFFFF2F2F2FFFFE8E8FFFFE9FFFFFFE9FFFFE8E8E9FFEAFFF5F1F5E8FFFFE8E8E8FFFF01E9E90AE8FFFF5CE8F8FF4341FFFF2F2BFFF1FDFFFDFFB0FFFFFF72E834FF73E801FFB8FFFFFFE9F1F1FF92E9B3F1FDFFFDFFE8E8FFFFEEFFFFFFFFE9FFFFFDFFFDFFA5FFFFFFE9E9E8FF9DFFFFFFE8E8FEFFE9E9FFFFE9E8F4FF77E8E9FFFFE9F5FFFE44FFFF22FFFFFFFFFFA1A142FFFFFFBFE8FFFFE9F0F0FFD1E9FFFFFEFFFFFFFFFFFFFFE8F2FFFFFFFF9BFFE9F8FFFFF0FFFFFFE9FFFFFFFFEBEBFFE8F4F4FFF2F2FBFFFFE9FFFFFF3838FFF5E9FFFFFFFFFFF1FFFAFAFFF0FFF0FFE8F3FFFFFFFFFFFFF5E9FFFFFFE8FFFFFFFFF6FF65FF65FFFDFFFDFFEAFFFFFF20FF1FFFFFFFFFFFFFFFF8FF6FE8FFFFA4FFFFFFA9FFFFFFE9FFE8FFF9FFF2FFE1FFFFFFFDFFFDFFEAFFFFFFFFF3FFFF5AE8FFFF7DFFB2FFABFFFFFFFFFFFFFFFFFFFFFF9FFFFFFFEEEA282841ADABFFEAFFFFFFFFFFFFFFEFFFFFFFE9F2F2FFFFFFFFF8FDFFFDFF36E8E8FFFFFDFFFFFFE9FFFFFF8DF2FFFFFFE9FFE9E85959F0FFF0FF11FFFFFFFFFFFFFFF0FFF0FFEAFFFFFF43FFFFFFFFE8F9FFFFF5E9FF363735FFCFFF03FFFFFFB4F889F7F7FFFDFFFDFFFFFFF8FFE9E9FFFFF0E8FFFF9EFFFFFFFFFFB4F8E9E8E9FFE8E8FFFFFFFBFCFFF2E9E9FF24FFFFFFFFE9FFFF45FFFFFFFFF1F7FF5DFFFFFF7CFF5DFFBFFFFFFFA6FFFFFFE8E8E8FFF9FFFFFF160AFFFF4A48FFFFF0FFFFFFF0F3FFFF59FFFFFFE8E8E8FFF0FFF0FFEEEBEBFF07FFFFFF38F8F8FFFFFFFBFF41ADACFFE9F4FFFFF0FFF0FFA8FFFFFFFFF2F0FFCEF0F0FFA3FFFFFFE9E9F5FFE8E8FFFF0700FFFFF0FFFFF1CBE9FFFF41ADABFFE8E8FFFFE9E8E9FFA4FFFFFFF0FFF0FFE8E8E8FFFFFFFFFF2825FFFFC3FFFFFFA5FFFFFFAAFFFFFFFFFFFFFF9CFF9CFFFFFFEBEBFFFF5858FFE9FFFF54E8FFFFA403EEEEA7FFFFFFFFFFF7F7C7B50473FFFFFFFFFFFFFFFF120C0D0E2EFFF7F761FFFFFFA3FFFFFFA7E9FFFFFFFFFFFFFFFFFFFFFFFFFFFFCA94FFFFFFEEC1C1FFFFFFFFFFFFFFFFFF0DFFFFCAEEEEEEFFFFFFFF2FFFA1A1FFFFFFFFFFFFFFFFD1EAFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDBFFC8C882FDFDFD312FD3D3EBFFEBFFFFFFFFFFDCFF32329CFF181893FF2323FFEFFFFFEBFFEBFFFFFFFFFFFFFFFFFFFFB4FFFFFF00FFFFEBFFEBFFFFFFF8F8EBFFEBFFECFFEBFFFFFFE9E9FFFF5858FFFF6E6EFFFFFFFFEFEE0808ECFFEBFF026BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBFFFFF0EBFFFFF060FFFFFF60FFFFFFECFFEBFFFFFFFFFFFFEDFFFFB3FFFFFFA7FFFFFFFFFFFFFFFFFF6868EEECB2B2FFFF9494EAFF3C3CE9E9FFFFFFFFF0D5FFE8E8FFFFFFCCCCFFFFCBCBFFFF1919FFFF3131FFFFE8FFFFFFF5F5FFFFD2D2FFEEFFFFFFEEFFFFFFEEFFFFFFEEFFFFFFEEFFFFFFEEFFFFFFEEFFFFFF1BFFFFFF1CFFFFFFFFFFFFFFFFFFFFFFFFFFFFECFFEBFFECFFEBFF8CE9A4FFCCEEEFEFFFFFFFFFFFFEFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB1F0F5FFFFFFFFFFFFFFFFFFFDFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE9E8FFFFFFE8E8FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFCC12FFFFFFFFFFFFFFFFFFFF"

bytes = bytes.fromhex(hex)

print(len(bytes))

countOnlyCommon = 0


pos = 0
common_empty = 0
rare_empty = 0
countOnlyCommon = 0
count = 0
while pos < len(bytes):
    stealRare = bytes[pos]
    stealCommon = bytes[pos+1]
    dropRare = bytes[pos+2]
    dropCommon = bytes[pos+3]

    if(stealRare == 0xFF and stealCommon != 0xFF):
    #    print(f"no rare {stealRare:x}, but has common {stealCommon:x} @ " + str(pos/4))
        countOnlyCommon = countOnlyCommon+1
    
    if(stealRare == 0xFF):
        rare_empty = rare_empty+1
    
    if(stealCommon == 0xFF):
        common_empty = common_empty+1
    pos = pos+4

    count = count+1

print(f"count: {count}")
print(f"steal Common empty: {common_empty} {(common_empty/count) * 100}")
print(f"steal rare empty: {rare_empty} {(rare_empty/count) * 100}")
print(f"count only common: {countOnlyCommon} {(countOnlyCommon/count) * 100}")


# no rare ff, but has common f2 @ 33.0
# no rare ff, but has common e9 @ 44.0
# no rare ff, but has common e8 @ 48.0
# no rare ff, but has common e8 @ 65.0
# no rare ff, but has common eb @ 67.0
# no rare ff, but has common f8 @ 73.0
# no rare ff, but has common e8 @ 75.0
# no rare ff, but has common fa @ 86.0
# no rare ff, but has common e8 @ 93.0
# no rare ff, but has common e9 @ 94.0
# no rare ff, but has common e9 @ 95.0
# no rare ff, but has common 1 @ 100.0
# no rare ff, but has common e9 @ 115.0
# no rare ff, but has common e9 @ 124.0
# no rare ff, but has common eb @ 139.0
# no rare ff, but has common e9 @ 142.0
# no rare ff, but has common 38 @ 143.0
# no rare ff, but has common fa @ 146.0
# no rare ff, but has common e8 @ 151.0
# no rare ff, but has common f3 @ 167.0
# no rare ff, but has common fd @ 183.0
# no rare ff, but has common e9 @ 184.0
# no rare ff, but has common 8d @ 185.0
# no rare ff, but has common e8 @ 194.0
# no rare ff, but has common f5 @ 195.0
# no rare ff, but has common fb @ 208.0
# no rare ff, but has common e9 @ 211.0
# no rare ff, but has common f1 @ 213.0
# no rare ff, but has common f2 @ 235.0
# no rare ff, but has common e9 @ 258.0
# no rare ff, but has common ee @ 275.0
# no rare ff, but has common d @ 278.0
# no rare ff, but has common ef @ 298.0
# no rare ff, but has common b4 @ 302.0
# no rare ff, but has common 0 @ 303.0
# no rare ff, but has common ed @ 325.0
# no rare ff, but has common e8 @ 335.0
# no rare ff, but has common ee @ 343.0
# no rare ff, but has common ee @ 344.0
# no rare ff, but has common ee @ 345.0
# no rare ff, but has common ee @ 346.0
# no rare ff, but has common ee @ 347.0
# no rare ff, but has common ee @ 348.0
# no rare ff, but has common ee @ 349.0
# no rare ff, but has common 1b @ 350.0
# no rare ff, but has common 1c @ 351.0
# no rare ff, but has common fe @ 360.0
# no rare ff, but has common e8 @ 374.0


# C2/399E: A3 05        LDA $05,S   (Attacker)
# C2/39A0: AA           TAX
# C2/39A1: A9 01        LDA #$01
# C2/39A3: 8D 01 34     STA $3401   (=1) (Sets message to "Doesn't have anything!")
# C2/39A6: E0 08        CPX #$08    (Check if attacker is monster)
# C2/39A8: B0 5F        BCS $3A09   (Branch if monster)
# C2/39AA: C2 20        REP #$20    (Set 16-bit accumulator)
# C2/39AC: B9 08 33     LDA $3308,Y (Target's stolen items)
# C2/39AF: 1A           INC
# C2/39B0: E2 21        SEP #$21    (Set 8-bit Accumulator AND Carry Flag)
# C2/39B2: F0 4D        BEQ $3A01   (Fail to steal if no items)
# C2/39B4: EE 01 34     INC $3401   (now = 2) (Sets message to "Couldn't steal!!")
# C2/39B7: BD 18 3B     LDA $3B18,X (Attacker's Level)
# C2/39BA: 69 32        ADC #$32    (adding 51, since Carry Flag was set)
# C2/39BC: B0 1A        BCS $39D8   (Automatically steal if level >= 205)
# C2/39BE: F9 18 3B     SBC $3B18,Y (Subtract Target's Level, along with an extra 1 because
#                                    Carry Flag is unset at this point.  Don't worry; this
#                                    cancels out with the extra 1 from C2/39BA.)

#                                   (StealValue = [attacker level + 51] - [target lvl + 1]
#                                    = Attacker level + 50 - Target level )

# C2/39C1: 90 3E        BCC $3A01   (Fail to steal if StealValue < 0)

# C2/39C3: 30 13        BMI $39D8   (Automatically steal if StealValue >= 128)
# C2/39C5: 85 EE        STA $EE     (save StealValue)
# C2/39C7: BD 45 3C     LDA $3C45,X
# C2/39CA: 4A           LSR
# C2/39CB: 90 02        BCC $39CF   (If no sneak ring)
# C2/39CD: 06 EE        ASL $EE     (Double value)
# C2/39CF: A9 64        LDA #$64
# C2/39D1: 20 65 4B     JSR $4B65   (Random: 0 to 99)
# C2/39D4: C5 EE        CMP $EE
# C2/39D6: B0 29        BCS $3A01   (Fail to steal if the random number >= StealValue)
# C2/39D8: 5A           PHY
# C2/39D9: 20 5A 4B     JSR $4B5A   (Random: 0 to 255)
# C2/39DC: C9 20        CMP #$20
# C2/39DE: 90 01        BCC $39E1   (branch 1/8 of the time, so Rare steal slot
#                                    will be checked)
# C2/39E0: C8           INY         (Check the 2nd [Common] slot 7/8 of the time)
# C2/39E1: B9 08 33     LDA $3308,Y (Target's stolen item)
# C2/39E4: 7A           PLY
# C2/39E5: C9 FF        CMP #$FF    (If no item)
# C2/39E7: F0 18        BEQ $3A01   (Fail to steal)
# C2/39E9: 8D 35 2F     STA $2F35   (Item stolen, for message purposes)
# C2/39EC: 9D F4 32     STA $32F4,X (Store in "Acquired item")
# C2/39EF: BD 18 30     LDA $3018,X
# C2/39F2: 0C 8C 3A     TSB $3A8C   (flag character to have any applicable item in
#                                    $32F4,X added to inventory when turn is over.)
# C2/39F5: A9 FF        LDA #$FF
# C2/39F7: 99 08 33     STA $3308,Y  (Set to no item to steal)
# C2/39FA: 99 09 33     STA $3309,Y  (in both slots)
# C2/39FD: EE 01 34     INC $3401    (now = 3) (Sets message to "Stole #whatever ")
# C2/3A00: 60           RTS


# Successful steal of rare
# c2399e lda $05,s      [0015da] A:0000 X:00a4 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:114 H:259 F: 0
# c239a0 tax                     A:0000 X:00a4 Y:0010 S:15d5 D:0000 DB:7e ..MX.IZ. V:114 H:266 F: 0
# c239a1 lda #$01                A:0000 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.IZ. V:114 H:269 F: 0
# c239a3 sta $3401      [7e3401] A:0001 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.. V:114 H:272 F: 0
# c239a6 cpx #$08                A:0001 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.. V:114 H:278 F: 0
# c239a8 bcs $3a09      [c23a09] A:0001 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:114 H:326 F: 0
# c239aa rep #$20                A:0001 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:114 H:328 F: 0
# c239ac lda $3308,y    [7e3318] A:0001 X:0000 Y:0010 S:15d5 D:0000 DB:7e N..X.I.. V:114 H:333 F: 0
# c239af inc                     A:e8e8 X:0000 Y:0010 S:15d5 D:0000 DB:7e N..X.I.. V:115 H:  1 F: 0
# c239b0 sep #$21                A:e8e9 X:0000 Y:0010 S:15d5 D:0000 DB:7e N..X.I.. V:115 H:  4 F: 0
# c239b2 beq $3a01      [c23a01] A:e8e9 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.C V:115 H:  9 F: 0
# c239b4 inc $3401      [7e3401] A:e8e9 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.C V:115 H: 12 F: 0
# c239b7 lda $3b18,x    [7e3b18] A:e8e9 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.C V:115 H: 22 F: 0
# c239ba adc #$ff                A:e805 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.C V:115 H: 28 F: 0
# c239bc bcs $39d8      [c239d8] A:e805 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.C V:115 H: 31 F: 0
# c239d8 phy                     A:e805 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.C V:115 H: 36 F: 0
# c239d9 jsr $4b5a      [c24b5a] A:e805 X:0000 Y:0010 S:15d4 D:0000 DB:7e ..MX.I.C V:115 H: 41 F: 0
# c24b5a phx                     A:e805 X:0000 Y:0010 S:15d2 D:0000 DB:7e ..MX.I.C V:115 H: 51 F: 0
# c24b5b inc $be        [0000be] A:e805 X:0000 Y:0010 S:15d1 D:0000 DB:7e ..MX.I.C V:115 H: 56 F: 0
# c24b5d ldx $be        [0000be] A:e805 X:0000 Y:0010 S:15d1 D:0000 DB:7e N.MX.I.C V:115 H: 64 F: 0
# c24b5f lda $c0fd00,x  [c0fd8f] A:e805 X:008f Y:0010 S:15d1 D:0000 DB:7e N.MX.I.C V:115 H: 69 F: 0
# c24b63 plx                     A:e8cc X:008f Y:0010 S:15d1 D:0000 DB:7e N.MX.I.C V:115 H: 77 F: 0
# c24b64 rts                     A:e8cc X:0000 Y:0010 S:15d2 D:0000 DB:7e ..MX.IZC V:115 H: 83 F: 0
# c239dc cmp #$ff                A:e8cc X:0000 Y:0010 S:15d4 D:0000 DB:7e ..MX.IZC V:115 H: 93 F: 0
# c239de bcc $39e1      [c239e1] A:e8cc X:0000 Y:0010 S:15d4 D:0000 DB:7e N.MX.I.. V:115 H: 96 F: 0
# c239e1 lda $3308,y    [7e3318] A:e8cc X:0000 Y:0010 S:15d4 D:0000 DB:7e N.MX.I.. V:115 H:101 F: 0
# c239e4 ply                     A:e8e8 X:0000 Y:0010 S:15d4 D:0000 DB:7e N.MX.I.. V:115 H:107 F: 0
# c239e5 cmp #$ff                A:e8e8 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.. V:115 H:114 F: 0
# c239e7 beq $3a01      [c23a01] A:e8e8 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:117 F: 0
# c239e9 sta $2f35      [7e2f35] A:e8e8 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:120 F: 0
# c239ec sta $32f4,x    [7e32f4] A:e8e8 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:126 F: 0
# c239ef lda $3018,x    [7e3018] A:e8e8 X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:144 F: 0
# c239f2 tsb $3a8c      [7e3a8c] A:e801 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.. V:115 H:151 F: 0
# c239f5 lda #$ff                A:e801 X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.IZ. V:115 H:161 F: 0
# c239f7 sta $3308,y    [7e3318] A:e8ff X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:164 F: 0
# c239fa sta $3309,y    [7e3319] A:e8ff X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:172 F: 0
# c239fd inc $3401      [7e3401] A:e8ff X:0000 Y:0010 S:15d5 D:0000 DB:7e N.MX.I.. V:115 H:180 F: 0
# c23a00 rts                     A:e8ff X:0000 Y:0010 S:15d5 D:0000 DB:7e ..MX.I.. V:115 H:190 F: 0
# c23889 plp                     A:e8ff X:0000 Y:0010 S:15d7 D:0000 DB:7e ..MX.I.. V:115 H:200 F: 0

# Failed to steal rare
# c2399e lda $05,s      [0015da] A:0000 X:00a4 Y:000e S:15d5 D:0000 DB:7e N.MX.I.. V:116 H:338 F: 3
# c239a0 tax                     A:0000 X:00a4 Y:000e S:15d5 D:0000 DB:7e ..MX.IZ. V:117 H:  4 F: 3
# c239a1 lda #$01                A:0000 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.IZ. V:117 H:  7 F: 3
# c239a3 sta $3401      [7e3401] A:0001 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.. V:117 H: 10 F: 3
# c239a6 cpx #$08                A:0001 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.. V:117 H: 17 F: 3
# c239a8 bcs $3a09      [c23a09] A:0001 X:0000 Y:000e S:15d5 D:0000 DB:7e N.MX.I.. V:117 H: 20 F: 3
# c239aa rep #$20                A:0001 X:0000 Y:000e S:15d5 D:0000 DB:7e N.MX.I.. V:117 H: 23 F: 3
# c239ac lda $3308,y    [7e3316] A:0001 X:0000 Y:000e S:15d5 D:0000 DB:7e N..X.I.. V:117 H: 27 F: 3
# c239af inc                     A:e8ff X:0000 Y:000e S:15d5 D:0000 DB:7e N..X.I.. V:117 H: 36 F: 3
# c239b0 sep #$21                A:e900 X:0000 Y:000e S:15d5 D:0000 DB:7e N..X.I.. V:117 H: 39 F: 3
# c239b2 beq $3a01      [c23a01] A:e900 X:0000 Y:000e S:15d5 D:0000 DB:7e N.MX.I.C V:117 H: 43 F: 3
# c239b4 inc $3401      [7e3401] A:e900 X:0000 Y:000e S:15d5 D:0000 DB:7e N.MX.I.C V:117 H: 46 F: 3
# c239b7 lda $3b18,x    [7e3b18] A:e900 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.C V:117 H: 56 F: 3
# c239ba adc #$ff                A:e905 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.C V:117 H: 63 F: 3
# c239bc bcs $39d8      [c239d8] A:e905 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.C V:117 H: 66 F: 3
# c239d8 phy                     A:e905 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.C V:117 H: 70 F: 3
# c239d9 jsr $4b5a      [c24b5a] A:e905 X:0000 Y:000e S:15d4 D:0000 DB:7e ..MX.I.C V:117 H: 75 F: 3
# c24b5a phx                     A:e905 X:0000 Y:000e S:15d2 D:0000 DB:7e ..MX.I.C V:117 H: 85 F: 3
# c24b5b inc $be        [0000be] A:e905 X:0000 Y:000e S:15d1 D:0000 DB:7e ..MX.I.C V:117 H: 90 F: 3
# c24b5d ldx $be        [0000be] A:e905 X:0000 Y:000e S:15d1 D:0000 DB:7e ..MX.I.C V:117 H: 99 F: 3
# c24b5f lda $c0fd00,x  [c0fd55] A:e905 X:0055 Y:000e S:15d1 D:0000 DB:7e ..MX.I.C V:117 H:104 F: 3
# c24b63 plx                     A:e9ad X:0055 Y:000e S:15d1 D:0000 DB:7e N.MX.I.C V:117 H:111 F: 3
# c24b64 rts                     A:e9ad X:0000 Y:000e S:15d2 D:0000 DB:7e ..MX.IZC V:117 H:118 F: 3
# c239dc cmp #$ff                A:e9ad X:0000 Y:000e S:15d4 D:0000 DB:7e ..MX.IZC V:117 H:128 F: 3
# c239de bcc $39e1      [c239e1] A:e9ad X:0000 Y:000e S:15d4 D:0000 DB:7e N.MX.I.. V:117 H:131 F: 3
# c239e1 lda $3308,y    [7e3316] A:e9ad X:0000 Y:000e S:15d4 D:0000 DB:7e N.MX.I.. V:117 H:145 F: 3
# c239e4 ply                     A:e9ff X:0000 Y:000e S:15d4 D:0000 DB:7e N.MX.I.. V:117 H:152 F: 3
# c239e5 cmp #$ff                A:e9ff X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.I.. V:117 H:158 F: 3
# c239e7 beq $3a01      [c23a01] A:e9ff X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.IZC V:117 H:161 F: 3
# c23a01 sep #$20                A:e9ff X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.IZC V:117 H:166 F: 3
# c23a03 lda #$00                A:e9ff X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.IZC V:117 H:170 F: 3
# c23a05 sta $3d48,y    [7e3d56] A:e900 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.IZC V:117 H:173 F: 3
# c23a08 rts                     A:e900 X:0000 Y:000e S:15d5 D:0000 DB:7e ..MX.IZC V:117 H:181 F: 3
# c23889 plp                     A:e900 X:0000 Y:000e S:15d7 D:0000 DB:7e ..MX.IZC V:117 H:191 F: 3