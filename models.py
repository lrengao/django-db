# coding: utf-8
from django.db import models
from conf.tbm import STATE as WORK_STATE

ShardAttributeRecord = dict()


class AttributeRecord(models.Model):

    LOC_STATE = (
        (0, '中间'),
        (1, '起点'),
        (2, '终点'),
    )

    K_STATE = (
        (0, '正常点'),
        (1, '状态或者换变化点'),
        (2, '0点到0点1分'),
        (3, '23点59分到24点'),
    )

    @classmethod
    def get_shard_model(cls, tbm_code_md5):

        class Meta:
            db_table = 'attribute_record_%s' % tbm_code_md5

        attrs = {
            '__module__': cls.__module__,
            'Meta': Meta,
        }
        return type(str('AttributeRecord_%s' % tbm_code_md5), (cls,), attrs)

    @classmethod
    def shard(cls, tbm_code_md5):
        assert tbm_code_md5, 'id is required!'
        if tbm_code_md5 in ShardAttributeRecord:
            return ShardAttributeRecord[tbm_code_md5]
        else:
            m = cls.get_shard_model(tbm_code_md5)
            ShardAttributeRecord[tbm_code_md5] = m
            return m

    class Meta:
        abstract = True

    tbm_code = models.CharField(max_length=150, verbose_name='tbm编码')
    cylinder = models.IntegerField(verbose_name='环')
    src_record_id = models.IntegerField(verbose_name='src_record的id')
    record_code = models.DateTimeField(verbose_name='记录编码')  # data time
    report_time = models.DateTimeField(verbose_name='上报时间')
    insert_time = models.DateTimeField(verbose_name='数据插入时间', auto_now_add=True, null=True)
    warning_check = models.BooleanField(default=False, verbose_name='是否经过告警检查')
    k_state = models.PositiveSmallIntegerField(verbose_name='K值变化时状态值',choices=K_STATE,default=0, db_index=True)
    work_state = models.PositiveSmallIntegerField(verbose_name='工作状态',choices=WORK_STATE)
    cyl_loc = models.PositiveSmallIntegerField(verbose_name='处于环位置',choices=LOC_STATE,default=0, db_index=True)
    a001 = models.FloatField(verbose_name='土压[上]/泥水舱压力[上]', null=True, blank=True)
    a002 = models.FloatField(verbose_name='土压[右上]/泥水舱压力[右上]', null=True, blank=True)
    a003 = models.FloatField(verbose_name='土压[右]/泥水舱压力[右]', null=True, blank=True)
    a004 = models.FloatField(verbose_name='土压[右下]/泥水舱压力[右下]', null=True, blank=True)
    a005 = models.FloatField(verbose_name='土压[下]/泥水舱压力[下]', null=True, blank=True)
    a006 = models.FloatField(verbose_name='土压[左下]/泥水舱压力[左下]', null=True, blank=True)
    a007 = models.FloatField(verbose_name='土压[左]/泥水舱压力[左]', null=True, blank=True)
    a008 = models.FloatField(verbose_name='土压[左上]/泥水舱压力[左上]', null=True, blank=True)
    a009 = models.FloatField(verbose_name='土压力[中部]/泥水舱压力[中部]', null=True, blank=True)
    b000 = models.FloatField(verbose_name='推进行程/推进行程', null=True, blank=True)
    b001 = models.FloatField(verbose_name='推进速度/推进速度', null=True, blank=True)
    b002 = models.FloatField(verbose_name='刀盘转速/刀盘转速', null=True, blank=True)
    b003 = models.FloatField(verbose_name='贯入度/贯入度', null=True, blank=True)
    b004 = models.FloatField(verbose_name='刀盘扭矩/刀盘扭矩', null=True, blank=True)
    b005 = models.FloatField(verbose_name='刀盘扭矩比/刀盘扭矩比', null=True, blank=True)
    b006 = models.FloatField(verbose_name='总推力/总推力', null=True, blank=True)
    b007 = models.FloatField(verbose_name='推进油压/推进油压', null=True, blank=True)
    b008 = models.FloatField(verbose_name='刀盘累计旋转圈数/刀盘累计旋转圈数', null=True, blank=True)
    b009 = models.FloatField(verbose_name='刀盘累计旋转距离/刀盘累计旋转距离', null=True, blank=True)
    b010 = models.FloatField(verbose_name='刀盘渗漏油温/刀盘渗漏油温', null=True, blank=True)
    b011 = models.FloatField(verbose_name='齿轮油温/齿轮油温', null=True, blank=True)
    b012 = models.FloatField(verbose_name='液压油箱油温/液压油箱油温', null=True, blank=True)
    b013 = models.FloatField(verbose_name='桥架拉力/桥架拉力', null=True, blank=True)
    b014 = models.FloatField(verbose_name='桥架油压/桥架油压', null=True, blank=True)
    b015 = models.FloatField(verbose_name='出土量/出土量', null=True, blank=True)
    b016 = models.FloatField(verbose_name='出土量/出土量', null=True, blank=True)
    b017 = models.FloatField(verbose_name='渣土温度/渣土温度', null=True, blank=True)
    c001 = models.FloatField(verbose_name='推进千斤顶行程[上]/推进千斤顶行程[上]', null=True, blank=True)
    c002 = models.FloatField(verbose_name='推进千斤顶行程[右上]/推进千斤顶行程[右上]', null=True, blank=True)
    c003 = models.FloatField(verbose_name='推进千斤顶行程[右]/推进千斤顶行程[右]', null=True, blank=True)
    c004 = models.FloatField(verbose_name='推进千斤顶行程[右下]/推进千斤顶行程[右下]', null=True, blank=True)
    c005 = models.FloatField(verbose_name='推进千斤顶行程[下]/推进千斤顶行程[下]', null=True, blank=True)
    c006 = models.FloatField(verbose_name='推进千斤顶行程[左下]/推进千斤顶行程[左下]', null=True, blank=True)
    c007 = models.FloatField(verbose_name='推进千斤顶行程[左]/推进千斤顶行程[左]', null=True, blank=True)
    c008 = models.FloatField(verbose_name='推进千斤顶行程[左上]/推进千斤顶行程[左上]', null=True, blank=True)
    c101 = models.FloatField(verbose_name='推进千斤顶油压[上]/推进千斤顶油压[上]', null=True, blank=True)
    c102 = models.FloatField(verbose_name='推进千斤顶油压[右上]/推进千斤顶油压[右上]', null=True, blank=True)
    c103 = models.FloatField(verbose_name='推进千斤顶油压[右]/推进千斤顶油压[右]', null=True, blank=True)
    c104 = models.FloatField(verbose_name='推进千斤顶油压[右下]/推进千斤顶油压[右下]', null=True, blank=True)
    c105 = models.FloatField(verbose_name='推进千斤顶油压[下]/推进千斤顶油压[下]', null=True, blank=True)
    c106 = models.FloatField(verbose_name='推进千斤顶油压[左下]/推进千斤顶油压[左下]', null=True, blank=True)
    c107 = models.FloatField(verbose_name='推进千斤顶油压[左]/推进千斤顶油压[左]', null=True, blank=True)
    c108 = models.FloatField(verbose_name='推进千斤顶油压[左上]/推进千斤顶油压[左上]', null=True, blank=True)
    c111 = models.FloatField(verbose_name='推进千斤顶推力[上]/推进千斤顶推力[上]', null=True, blank=True)
    c112 = models.FloatField(verbose_name='推进千斤顶推力[右上]/推进千斤顶推力[右上]', null=True, blank=True)
    c113 = models.FloatField(verbose_name='推进千斤顶推力[右]/推进千斤顶推力[右]', null=True, blank=True)
    c114 = models.FloatField(verbose_name='推进千斤顶推力[右下]/推进千斤顶推力[右下]', null=True, blank=True)
    c115 = models.FloatField(verbose_name='推进千斤顶推力[下]/推进千斤顶推力[下]', null=True, blank=True)
    c116 = models.FloatField(verbose_name='推进千斤顶推力[左下]/推进千斤顶推力[左下]', null=True, blank=True)
    c117 = models.FloatField(verbose_name='推进千斤顶推力[左]/推进千斤顶推力[左]', null=True, blank=True)
    c118 = models.FloatField(verbose_name='推进千斤顶推力[左上]/推进千斤顶推力[左上]', null=True, blank=True)
    c201 = models.FloatField(verbose_name='推进千斤顶速度[上]/', null=True, blank=True)
    c202 = models.FloatField(verbose_name='推进千斤顶速度[右上]/', null=True, blank=True)
    c203 = models.FloatField(verbose_name='推进千斤顶速度[右]/', null=True, blank=True)
    c204 = models.FloatField(verbose_name='推进千斤顶速度[右下]/', null=True, blank=True)
    c205 = models.FloatField(verbose_name='推进千斤顶速度[下]/', null=True, blank=True)
    c206 = models.FloatField(verbose_name='推进千斤顶速度[左下]/', null=True, blank=True)
    c207 = models.FloatField(verbose_name='推进千斤顶速度[左]/', null=True, blank=True)
    c208 = models.FloatField(verbose_name='推进千斤顶速度[左上]/', null=True, blank=True)
    d000 = models.FloatField(verbose_name='同步注浆累计/同步注浆累计', null=True, blank=True)
    d001 = models.FloatField(verbose_name='同步注浆量A液/同步注浆量A液', null=True, blank=True)
    d002 = models.FloatField(verbose_name='同步注浆量B液/同步注浆量B液', null=True, blank=True)
    d003 = models.FloatField(verbose_name='二次注浆量/二次注浆量', null=True, blank=True)
    d101 = models.FloatField(verbose_name='同步注浆量[上]/同步注浆量[上]', null=True, blank=True)
    d102 = models.FloatField(verbose_name='同步注浆量[右上]/同步注浆量[右上]', null=True, blank=True)
    d103 = models.FloatField(verbose_name='同步注浆量[右]/同步注浆量[右]', null=True, blank=True)
    d104 = models.FloatField(verbose_name='同步注浆量[右下]/同步注浆量[右下]', null=True, blank=True)
    d105 = models.FloatField(verbose_name='同步注浆量[下]/同步注浆量[下]', null=True, blank=True)
    d106 = models.FloatField(verbose_name='同步注浆量[左下]/同步注浆量[左下]', null=True, blank=True)
    d107 = models.FloatField(verbose_name='同步注浆量[左]/同步注浆量[左]', null=True, blank=True)
    d108 = models.FloatField(verbose_name='同步注浆量[左上]/同步注浆量[左上]', null=True, blank=True)
    d201 = models.FloatField(verbose_name='同步注浆压力[上]/同步注浆压力[上]', null=True, blank=True)
    d202 = models.FloatField(verbose_name='同步注浆压力[右上]/同步注浆压力[右上]', null=True, blank=True)
    d203 = models.FloatField(verbose_name='同步注浆压力[右]/同步注浆压力[右]', null=True, blank=True)
    d204 = models.FloatField(verbose_name='同步注浆压力[右下]/同步注浆压力[右下]', null=True, blank=True)
    d205 = models.FloatField(verbose_name='同步注浆压力[下]/同步注浆压力[下]', null=True, blank=True)
    d206 = models.FloatField(verbose_name='同步注浆压力[左下]/同步注浆压力[左下]', null=True, blank=True)
    d207 = models.FloatField(verbose_name='同步注浆压力[左]/同步注浆压力[左]', null=True, blank=True)
    d208 = models.FloatField(verbose_name='同步注浆压力[左上]/同步注浆压力[左上]', null=True, blank=True)
    e001 = models.FloatField(verbose_name='铰接油缸行程[上]/铰接油缸行程[上]', null=True, blank=True)
    e002 = models.FloatField(verbose_name='铰接油缸行程[右上]/铰接油缸行程[右上]', null=True, blank=True)
    e003 = models.FloatField(verbose_name='铰接油缸行程[右]/铰接油缸行程[右]', null=True, blank=True)
    e004 = models.FloatField(verbose_name='铰接油缸行程[右下]/铰接油缸行程[右下]', null=True, blank=True)
    e005 = models.FloatField(verbose_name='铰接油缸行程[下]/铰接油缸行程[下]', null=True, blank=True)
    e006 = models.FloatField(verbose_name='铰接油缸行程[左下]/铰接油缸行程[左下]', null=True, blank=True)
    e007 = models.FloatField(verbose_name='铰接油缸行程[左]/铰接油缸行程[左]', null=True, blank=True)
    e008 = models.FloatField(verbose_name='铰接油缸行程[左上]/铰接油缸行程[左上]', null=True, blank=True)
    e101 = models.FloatField(verbose_name='铰接油缸油压[上]/铰接油缸油压[上]', null=True, blank=True)
    e102 = models.FloatField(verbose_name='铰接油缸油压[右上]/铰接油缸油压[右上]', null=True, blank=True)
    e103 = models.FloatField(verbose_name='铰接油缸油压[右]/铰接油缸油压[右]', null=True, blank=True)
    e104 = models.FloatField(verbose_name='铰接油缸油压[右下]/铰接油缸油压[右下]', null=True, blank=True)
    e105 = models.FloatField(verbose_name='铰接油缸油压[下]/铰接油缸油压[下]', null=True, blank=True)
    e106 = models.FloatField(verbose_name='铰接油缸油压[左下]/铰接油缸油压[左下]', null=True, blank=True)
    e107 = models.FloatField(verbose_name='铰接油缸油压[左]/铰接油缸油压[左]', null=True, blank=True)
    e108 = models.FloatField(verbose_name='铰接油缸油压[左上]/铰接油缸油压[左上]', null=True, blank=True)
    e201 = models.FloatField(verbose_name='铰接上下角/铰接上下角', null=True, blank=True)
    e202 = models.FloatField(verbose_name='铰接左右角/铰接左右角', null=True, blank=True)
    f001 = models.FloatField(verbose_name='螺旋输送机转速/', null=True, blank=True)
    f002 = models.FloatField(verbose_name='螺旋输送机扭矩/', null=True, blank=True)
    f003 = models.FloatField(verbose_name='螺旋输送机前端土压/', null=True, blank=True)
    f004 = models.FloatField(verbose_name='螺旋输送机后端土压/', null=True, blank=True)
    f005 = models.FloatField(verbose_name='螺旋输送机油压/', null=True, blank=True)
    f006 = models.FloatField(verbose_name='螺旋输送机封门开度/', null=True, blank=True)
    f007 = models.FloatField(verbose_name='螺旋输送机封门开度/', null=True, blank=True)
    f008 = models.FloatField(verbose_name='螺旋输送机渗漏油温/', null=True, blank=True)
    g000 = models.FloatField(verbose_name='盾尾油脂量/盾尾油脂量', null=True, blank=True)
    g001 = models.FloatField(verbose_name='前舱盾尾油脂量/前舱盾尾油脂量', null=True, blank=True)
    g002 = models.FloatField(verbose_name='后舱盾尾油脂量/中舱盾尾油脂量', null=True, blank=True)
    g003 = models.FloatField(verbose_name='/后舱盾尾油脂量', null=True, blank=True)
    g101 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[上]/盾尾密封油脂前舱压力1', null=True, blank=True)
    g102 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[右上]/盾尾密封油脂前舱压力2', null=True, blank=True)
    g103 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[右]/盾尾密封油脂前舱压力3', null=True, blank=True)
    g104 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[右下]/盾尾密封油脂前舱压力4', null=True, blank=True)
    g105 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[下]/盾尾密封油脂前舱压力5', null=True, blank=True)
    g106 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[左下]/盾尾密封油脂前舱压力6', null=True, blank=True)
    g107 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[左]/盾尾密封油脂前舱压力7', null=True, blank=True)
    g108 = models.FloatField(verbose_name='盾尾密封油脂前舱压力[左上]/盾尾密封油脂前舱压力8', null=True, blank=True)
    g109 = models.FloatField(verbose_name='/盾尾密封油脂前舱压力9', null=True, blank=True)
    g110 = models.FloatField(verbose_name='/盾尾密封油脂前舱压力10', null=True, blank=True)
    g111 = models.FloatField(verbose_name='/盾尾密封油脂前舱压力11', null=True, blank=True)
    g112 = models.FloatField(verbose_name='/盾尾密封油脂前舱压力12', null=True, blank=True)
    g201 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[上]/盾尾密封油脂中舱压力1', null=True, blank=True)
    g202 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[右上]/盾尾密封油脂中舱压力2', null=True, blank=True)
    g203 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[右]/盾尾密封油脂中舱压力3', null=True, blank=True)
    g204 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[右下]/盾尾密封油脂中舱压力4', null=True, blank=True)
    g205 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[下]/盾尾密封油脂中舱压力5', null=True, blank=True)
    g206 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[左下]/盾尾密封油脂中舱压力6', null=True, blank=True)
    g207 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[左]/盾尾密封油脂中舱压力7', null=True, blank=True)
    g208 = models.FloatField(verbose_name='盾尾密封油脂后舱压力[左上]/盾尾密封油脂中舱压力8', null=True, blank=True)
    g209 = models.FloatField(verbose_name='/盾尾密封油脂中舱压力9', null=True, blank=True)
    g210 = models.FloatField(verbose_name='/盾尾密封油脂中舱压力10', null=True, blank=True)
    g211 = models.FloatField(verbose_name='/盾尾密封油脂中舱压力11', null=True, blank=True)
    g212 = models.FloatField(verbose_name='/盾尾密封油脂中舱压力12', null=True, blank=True)
    g301 = models.FloatField(verbose_name='盾尾密封油脂前舱量[上]/盾尾密封油脂后舱压力1', null=True, blank=True)
    g302 = models.FloatField(verbose_name='盾尾密封油脂前舱量[右上]/盾尾密封油脂后舱压力2', null=True, blank=True)
    g303 = models.FloatField(verbose_name='盾尾密封油脂前舱量[右]/盾尾密封油脂后舱压力3', null=True, blank=True)
    g304 = models.FloatField(verbose_name='盾尾密封油脂前舱量[右下]/盾尾密封油脂后舱压力4', null=True, blank=True)
    g305 = models.FloatField(verbose_name='盾尾密封油脂前舱量[下]/盾尾密封油脂后舱压力5', null=True, blank=True)
    g306 = models.FloatField(verbose_name='盾尾密封油脂前舱量[左下]/盾尾密封油脂后舱压力6', null=True, blank=True)
    g307 = models.FloatField(verbose_name='盾尾密封油脂前舱量[左]/盾尾密封油脂后舱压力7', null=True, blank=True)
    g308 = models.FloatField(verbose_name='盾尾密封油脂前舱量[左上]/盾尾密封油脂后舱压力8', null=True, blank=True)
    g309 = models.FloatField(verbose_name='/盾尾密封油脂后舱压力9', null=True, blank=True)
    g310 = models.FloatField(verbose_name='/盾尾密封油脂后舱压力10', null=True, blank=True)
    g311 = models.FloatField(verbose_name='/盾尾密封油脂后舱压力11', null=True, blank=True)
    g312 = models.FloatField(verbose_name='/盾尾密封油脂后舱压力12', null=True, blank=True)
    g401 = models.FloatField(verbose_name='盾尾密封油脂后舱量[上]/盾尾密封油脂前舱量1', null=True, blank=True)
    g402 = models.FloatField(verbose_name='盾尾密封油脂后舱量[右上]/盾尾密封油脂前舱量2', null=True, blank=True)
    g403 = models.FloatField(verbose_name='盾尾密封油脂后舱量[右]/盾尾密封油脂前舱量3', null=True, blank=True)
    g404 = models.FloatField(verbose_name='盾尾密封油脂后舱量[右下]/盾尾密封油脂前舱量4', null=True, blank=True)
    g405 = models.FloatField(verbose_name='盾尾密封油脂后舱量[下]/盾尾密封油脂前舱量5', null=True, blank=True)
    g406 = models.FloatField(verbose_name='盾尾密封油脂后舱量[左下]/盾尾密封油脂前舱量6', null=True, blank=True)
    g407 = models.FloatField(verbose_name='盾尾密封油脂后舱量[左]/盾尾密封油脂前舱量7', null=True, blank=True)
    g408 = models.FloatField(verbose_name='盾尾密封油脂后舱量[左上]/盾尾密封油脂前舱量8', null=True, blank=True)
    g409 = models.FloatField(verbose_name='/盾尾密封油脂前舱量9', null=True, blank=True)
    g410 = models.FloatField(verbose_name='/盾尾密封油脂前舱量10', null=True, blank=True)
    g411 = models.FloatField(verbose_name='/盾尾密封油脂前舱量11', null=True, blank=True)
    g412 = models.FloatField(verbose_name='/盾尾密封油脂前舱量12', null=True, blank=True)
    g501 = models.FloatField(verbose_name='/盾尾密封油脂中舱量1', null=True, blank=True)
    g502 = models.FloatField(verbose_name='/盾尾密封油脂中舱量2', null=True, blank=True)
    g503 = models.FloatField(verbose_name='/盾尾密封油脂中舱量3', null=True, blank=True)
    g504 = models.FloatField(verbose_name='/盾尾密封油脂中舱量4', null=True, blank=True)
    g505 = models.FloatField(verbose_name='/盾尾密封油脂中舱量5', null=True, blank=True)
    g506 = models.FloatField(verbose_name='/盾尾密封油脂中舱量6', null=True, blank=True)
    g507 = models.FloatField(verbose_name='/盾尾密封油脂中舱量7', null=True, blank=True)
    g508 = models.FloatField(verbose_name='/盾尾密封油脂中舱量8', null=True, blank=True)
    g509 = models.FloatField(verbose_name='/盾尾密封油脂中舱量9', null=True, blank=True)
    g510 = models.FloatField(verbose_name='/盾尾密封油脂中舱量10', null=True, blank=True)
    g511 = models.FloatField(verbose_name='/盾尾密封油脂中舱量11', null=True, blank=True)
    g512 = models.FloatField(verbose_name='/盾尾密封油脂中舱量12', null=True, blank=True)
    g601 = models.FloatField(verbose_name='/盾尾密封油脂后舱量1', null=True, blank=True)
    g602 = models.FloatField(verbose_name='/盾尾密封油脂后舱量2', null=True, blank=True)
    g603 = models.FloatField(verbose_name='/盾尾密封油脂后舱量3', null=True, blank=True)
    g604 = models.FloatField(verbose_name='/盾尾密封油脂后舱量4', null=True, blank=True)
    g605 = models.FloatField(verbose_name='/盾尾密封油脂后舱量5', null=True, blank=True)
    g606 = models.FloatField(verbose_name='/盾尾密封油脂后舱量6', null=True, blank=True)
    g607 = models.FloatField(verbose_name='/盾尾密封油脂后舱量7', null=True, blank=True)
    g608 = models.FloatField(verbose_name='/盾尾密封油脂后舱量8', null=True, blank=True)
    g609 = models.FloatField(verbose_name='/盾尾密封油脂后舱量9', null=True, blank=True)
    g610 = models.FloatField(verbose_name='/盾尾密封油脂后舱量10', null=True, blank=True)
    g611 = models.FloatField(verbose_name='/盾尾密封油脂后舱量11', null=True, blank=True)
    g612 = models.FloatField(verbose_name='/盾尾密封油脂后舱量12', null=True, blank=True)
    h000 = models.FloatField(verbose_name='总泡沫量/HBW密封油脂总量', null=True, blank=True)
    h001 = models.FloatField(verbose_name='泡沫添加剂配比/HBW密封油脂泵压力', null=True, blank=True)
    h002 = models.FloatField(verbose_name='泡沫添加剂设定流量/', null=True, blank=True)
    h003 = models.FloatField(verbose_name='泡沫添加剂流量/', null=True, blank=True)
    h004 = models.FloatField(verbose_name='泡沫系统水泵流量/', null=True, blank=True)
    h005 = models.FloatField(verbose_name='泡沫添加剂累计/', null=True, blank=True)
    h006 = models.FloatField(verbose_name='泡沫系统水累计/', null=True, blank=True)
    h101 = models.FloatField(verbose_name='No1泡沫压力/', null=True, blank=True)
    h102 = models.FloatField(verbose_name='No1泡沫气体流量/', null=True, blank=True)
    h103 = models.FloatField(verbose_name='No1泡沫液体流量/', null=True, blank=True)
    h104 = models.FloatField(verbose_name='No1泡沫累计/', null=True, blank=True)
    h111 = models.FloatField(verbose_name='/HBW油脂外部密封1流量', null=True, blank=True)
    h112 = models.FloatField(verbose_name='/HBW油脂外部密封1压力', null=True, blank=True)
    h121 = models.FloatField(verbose_name='/HBW油脂外部密封2流量', null=True, blank=True)
    h122 = models.FloatField(verbose_name='/HBW油脂外部密封2压力', null=True, blank=True)
    h201 = models.FloatField(verbose_name='No2泡沫压力/HBW油脂内部密封1压力', null=True, blank=True)
    h202 = models.FloatField(verbose_name='No2泡沫气体流量/HBW油脂内部密封2压力', null=True, blank=True)
    h203 = models.FloatField(verbose_name='No2泡沫液体流量/HBW油脂内部密封流量 ', null=True, blank=True)
    h204 = models.FloatField(verbose_name='No2泡沫累计/', null=True, blank=True)
    h301 = models.FloatField(verbose_name='No3泡沫压力/', null=True, blank=True)
    h302 = models.FloatField(verbose_name='No3泡沫气体流量/', null=True, blank=True)
    h303 = models.FloatField(verbose_name='No3泡沫液体流量/', null=True, blank=True)
    h304 = models.FloatField(verbose_name='No3泡沫累计/', null=True, blank=True)
    h401 = models.FloatField(verbose_name='No4泡沫压力/', null=True, blank=True)
    h402 = models.FloatField(verbose_name='No4泡沫气体流量/', null=True, blank=True)
    h403 = models.FloatField(verbose_name='No4泡沫液体流量/', null=True, blank=True)
    h404 = models.FloatField(verbose_name='No4泡沫累计/', null=True, blank=True)
    h501 = models.FloatField(verbose_name='No5泡沫压力/', null=True, blank=True)
    h502 = models.FloatField(verbose_name='No5泡沫气体流量/', null=True, blank=True)
    h503 = models.FloatField(verbose_name='No5泡沫液体流量/', null=True, blank=True)
    h504 = models.FloatField(verbose_name='No5泡沫累计/', null=True, blank=True)
    h601 = models.FloatField(verbose_name='No6泡沫压力/', null=True, blank=True)
    h602 = models.FloatField(verbose_name='No6泡沫气体流量/', null=True, blank=True)
    h603 = models.FloatField(verbose_name='No6泡沫液体流量/', null=True, blank=True)
    h604 = models.FloatField(verbose_name='No6泡沫累计/', null=True, blank=True)
    h701 = models.FloatField(verbose_name='No7泡沫压力/', null=True, blank=True)
    h702 = models.FloatField(verbose_name='No7泡沫气体流量/', null=True, blank=True)
    h703 = models.FloatField(verbose_name='No7泡沫液体流量/', null=True, blank=True)
    h704 = models.FloatField(verbose_name='No7泡沫累计/', null=True, blank=True)
    h801 = models.FloatField(verbose_name='No8泡沫压力/', null=True, blank=True)
    h802 = models.FloatField(verbose_name='No8泡沫气体流量/', null=True, blank=True)
    h803 = models.FloatField(verbose_name='No8泡沫液体流量/', null=True, blank=True)
    h804 = models.FloatField(verbose_name='No8泡沫累计/', null=True, blank=True)
    i000 = models.FloatField(verbose_name='膨润土量/润滑油脂总量', null=True, blank=True)
    i001 = models.FloatField(verbose_name='/润滑油脂泵流量', null=True, blank=True)
    i002 = models.FloatField(verbose_name='/润滑油脂泵压力', null=True, blank=True)
    i101 = models.FloatField(verbose_name='No1膨润土压力/', null=True, blank=True)
    i102 = models.FloatField(verbose_name='No1膨润土流量/', null=True, blank=True)
    i103 = models.FloatField(verbose_name='No1膨润土累计/', null=True, blank=True)
    i111 = models.FloatField(verbose_name='/润滑油脂外部01流速', null=True, blank=True)
    i112 = models.FloatField(verbose_name='/润滑油脂外部01油压', null=True, blank=True)
    i121 = models.FloatField(verbose_name='/润滑油脂内部01流速', null=True, blank=True)
    i122 = models.FloatField(verbose_name='/润滑油脂内部01油压', null=True, blank=True)
    i201 = models.FloatField(verbose_name='No2膨润土压力/', null=True, blank=True)
    i202 = models.FloatField(verbose_name='No2膨润土流量/', null=True, blank=True)
    i203 = models.FloatField(verbose_name='No2膨润土累计/', null=True, blank=True)
    i211 = models.FloatField(verbose_name='/润滑油脂外部02流速', null=True, blank=True)
    i212 = models.FloatField(verbose_name='/润滑油脂外部02油压', null=True, blank=True)
    i221 = models.FloatField(verbose_name='/润滑油脂内部02流速', null=True, blank=True)
    i222 = models.FloatField(verbose_name='/润滑油脂内部02油压', null=True, blank=True)
    i301 = models.FloatField(verbose_name='No3膨润土压力/', null=True, blank=True)
    i302 = models.FloatField(verbose_name='No3膨润土流量/', null=True, blank=True)
    i303 = models.FloatField(verbose_name='No3膨润土累计/', null=True, blank=True)
    i311 = models.FloatField(verbose_name='/润滑油脂外部03流速', null=True, blank=True)
    i312 = models.FloatField(verbose_name='/润滑油脂外部03油压', null=True, blank=True)
    i321 = models.FloatField(verbose_name='/润滑油脂内部03流速', null=True, blank=True)
    i322 = models.FloatField(verbose_name='/润滑油脂内部03油压', null=True, blank=True)
    i401 = models.FloatField(verbose_name='No4膨润土压力/', null=True, blank=True)
    i402 = models.FloatField(verbose_name='No4膨润土流量/', null=True, blank=True)
    i403 = models.FloatField(verbose_name='No4膨润土累计/', null=True, blank=True)
    i501 = models.FloatField(verbose_name='No5膨润土压力/', null=True, blank=True)
    i502 = models.FloatField(verbose_name='No5膨润土流量/', null=True, blank=True)
    i503 = models.FloatField(verbose_name='No5膨润土累计/', null=True, blank=True)
    i601 = models.FloatField(verbose_name='No6膨润土压力/', null=True, blank=True)
    i602 = models.FloatField(verbose_name='No6膨润土流量/', null=True, blank=True)
    i603 = models.FloatField(verbose_name='No6膨润土累计/', null=True, blank=True)
    j001 = models.FloatField(verbose_name='里程/里程', null=True, blank=True)
    j111 = models.FloatField(verbose_name='前盾X坐标/前盾X坐标', null=True, blank=True)
    j112 = models.FloatField(verbose_name='前盾Y坐标/前盾Y坐标', null=True, blank=True)
    j113 = models.FloatField(verbose_name='前盾Z坐标/前盾Z坐标', null=True, blank=True)
    j121 = models.FloatField(verbose_name='中盾X坐标/中盾X坐标', null=True, blank=True)
    j122 = models.FloatField(verbose_name='中盾Y坐标/中盾Y坐标', null=True, blank=True)
    j123 = models.FloatField(verbose_name='中盾Z坐标/中盾Z坐标', null=True, blank=True)
    j131 = models.FloatField(verbose_name='尾盾X坐标/尾盾X坐标', null=True, blank=True)
    j132 = models.FloatField(verbose_name='尾盾Y坐标/尾盾Y坐标', null=True, blank=True)
    j133 = models.FloatField(verbose_name='尾盾Z坐标/尾盾Z坐标', null=True, blank=True)
    j201 = models.FloatField(verbose_name='滚动角/滚动角', null=True, blank=True)
    j211 = models.FloatField(verbose_name='前盾体俯仰角/前盾体俯仰角', null=True, blank=True)
    j212 = models.FloatField(verbose_name='前盾体水平角/前盾体水平角', null=True, blank=True)
    j221 = models.FloatField(verbose_name='后盾体俯仰角/后盾体俯仰角', null=True, blank=True)
    j222 = models.FloatField(verbose_name='后盾体水平角/后盾体水平角', null=True, blank=True)
    j301 = models.FloatField(verbose_name='前盾体水平偏角/前盾体水平偏角', null=True, blank=True)
    j302 = models.FloatField(verbose_name='前盾体竖直偏角/前盾体竖直偏角', null=True, blank=True)
    j311 = models.FloatField(verbose_name='后盾体水平偏角/后盾体水平偏角', null=True, blank=True)
    j312 = models.FloatField(verbose_name='后盾体竖直偏角/后盾体竖直偏角', null=True, blank=True)
    j411 = models.FloatField(verbose_name='前盾水平偏差/前盾水平偏差', null=True, blank=True)
    j412 = models.FloatField(verbose_name='前盾垂直偏差/前盾垂直偏差', null=True, blank=True)
    j421 = models.FloatField(verbose_name='中盾水平偏差/中盾水平偏差', null=True, blank=True)
    j422 = models.FloatField(verbose_name='中盾垂直偏差/中盾垂直偏差', null=True, blank=True)
    j431 = models.FloatField(verbose_name='尾盾水平偏差/尾盾水平偏差', null=True, blank=True)
    j432 = models.FloatField(verbose_name='尾盾垂直偏差/尾盾垂直偏差', null=True, blank=True)
    k001 = models.FloatField(verbose_name='停止时间/停止时间', null=True, blank=True)
    k002 = models.FloatField(verbose_name='推进时间/推进时间', null=True, blank=True)
    k003 = models.FloatField(verbose_name='拼装时间/拼装时间', null=True, blank=True)
    l001 = models.FloatField(verbose_name='土舱氧气含量（O2）/土舱氧气含量（O2）', null=True, blank=True)
    l002 = models.FloatField(verbose_name='土舱一氧化碳含量（CO）/土舱一氧化碳含量（CO）', null=True, blank=True)
    l003 = models.FloatField(verbose_name='土舱二氧化碳含量（CO2）/土舱二氧化碳含量（CO2）', null=True, blank=True)
    l004 = models.FloatField(verbose_name='土舱甲烷含量（CH4）/土舱甲烷含量（CH4）', null=True, blank=True)
    l005 = models.FloatField(verbose_name='土舱一氧化氮含量（NO）/土舱一氧化氮含量（NO）', null=True, blank=True)
    l201 = models.FloatField(verbose_name='台车氧气含量（O2）/台车氧气含量（O2）', null=True, blank=True)
    l202 = models.FloatField(verbose_name='台车一氧化碳含量（CO）/台车一氧化碳含量（CO）', null=True, blank=True)
    l203 = models.FloatField(verbose_name='台车二氧化碳含量（CO2）/台车二氧化碳含量（CO2）', null=True, blank=True)
    l204 = models.FloatField(verbose_name='台车甲烷含量（CH4）/台车甲烷含量（CH4）', null=True, blank=True)
    l205 = models.FloatField(verbose_name='台车一氧化氮含量（NO）/台车一氧化氮含量（NO）', null=True, blank=True)
    m000 = models.FloatField(verbose_name='/上部土压1', null=True, blank=True)
    m001 = models.FloatField(verbose_name='/上部土压2', null=True, blank=True)
    m002 = models.FloatField(verbose_name='/中部土压', null=True, blank=True)
    m003 = models.FloatField(verbose_name='/气垫仓压力', null=True, blank=True)
    m011 = models.FloatField(verbose_name='/气垫仓L液位', null=True, blank=True)
    m012 = models.FloatField(verbose_name='/气垫仓R液位', null=True, blank=True)
    m021 = models.FloatField(verbose_name='/P0.1转速', null=True, blank=True)
    m022 = models.FloatField(verbose_name='/P0.2转速', null=True, blank=True)
    m023 = models.FloatField(verbose_name='/P1.1转速', null=True, blank=True)
    m024 = models.FloatField(verbose_name='/P2.1转速', null=True, blank=True)
    m101 = models.FloatField(verbose_name='/P0.1压力', null=True, blank=True)
    m102 = models.FloatField(verbose_name='/P0.2压力', null=True, blank=True)
    m111 = models.FloatField(verbose_name='/P1.1进口压力', null=True, blank=True)
    m112 = models.FloatField(verbose_name='/P1.1出口压力', null=True, blank=True)
    m121 = models.FloatField(verbose_name='/P2.1进口压力', null=True, blank=True)
    m122 = models.FloatField(verbose_name='/P2.1出口压力', null=True, blank=True)
    m201 = models.FloatField(verbose_name='/进浆流量', null=True, blank=True)
    m202 = models.FloatField(verbose_name='/排浆流量', null=True, blank=True)
    m301 = models.FloatField(verbose_name='/外循环进水温度', null=True, blank=True)
    m302 = models.FloatField(verbose_name='/外循环回水温度', null=True, blank=True)
    v001 = models.FloatField(verbose_name='/阀F1的状态指示', null=True, blank=True)
    v003 = models.FloatField(verbose_name='/阀F3的状态指示', null=True, blank=True)
    v004 = models.FloatField(verbose_name='/阀F4的状态指示', null=True, blank=True)
    v005 = models.FloatField(verbose_name='/阀F5的状态指示', null=True, blank=True)
    v006 = models.FloatField(verbose_name='/阀F6的状态指示', null=True, blank=True)
    v007 = models.FloatField(verbose_name='/阀F7的状态指示', null=True, blank=True)
    v008 = models.FloatField(verbose_name='/阀F8的状态指示', null=True, blank=True)
    v009 = models.FloatField(verbose_name='/阀F9的状态指示', null=True, blank=True)
    v010 = models.FloatField(verbose_name='/阀F10的状态指示', null=True, blank=True)
    v011 = models.FloatField(verbose_name='/阀F11的状态指示', null=True, blank=True)
    v012 = models.FloatField(verbose_name='/阀F12的状态指示', null=True, blank=True)
    v017 = models.FloatField(verbose_name='/阀F17的状态指示', null=True, blank=True)
    v018 = models.FloatField(verbose_name='/阀F18的状态指示', null=True, blank=True)
    v030 = models.FloatField(verbose_name='/阀F30的状态指示', null=True, blank=True)
    v031 = models.FloatField(verbose_name='/阀F31的状态指示', null=True, blank=True)
    v032 = models.FloatField(verbose_name='/阀F32的状态指示', null=True, blank=True)
    v037 = models.FloatField(verbose_name='/阀F37的状态指示', null=True, blank=True)
    v038 = models.FloatField(verbose_name='/阀F38的状态指示', null=True, blank=True)
    v050 = models.FloatField(verbose_name='/阀F50的状态指示', null=True, blank=True)
    v051 = models.FloatField(verbose_name='/阀F51的状态指示', null=True, blank=True)


