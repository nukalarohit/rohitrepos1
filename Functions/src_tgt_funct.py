def src_tgt_cmpr(src_cnt,tgt_cnt):
    if src_cnt==tgt_cnt:
        print(f"src count{src_cnt}  is matching with target count {tgt_cnt}")
    else:
        print("src and tgt count is not matching and the difference is:")
    return src_cnt-tgt_cnt,src_cnt+tgt_cnt

s=int(input('enter the src count:'))
t=int(input('enter the tgt count:'))
print('the difference is :',src_tgt_cmpr(s,t),type(src_tgt_cmpr(s,t)))
