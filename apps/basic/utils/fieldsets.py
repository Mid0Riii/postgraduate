EmploymentFieldSets = (
    ["学生信息", {
        'fields': (
            "emp_id", "emp_stu", "emp_gender", "emp_loc"
        ),
    }
     ],
    ["就业信息", {
        'fields': (
            'emp_type',
            'emp_direction',
            'emp_sign_type',
            'emp_sign_unit',
            'emp_sign_loc',
            ('emp_file_unit', 'emp_file_phone'),
            ('emp_file_loc', 'emp_file_postcode'),
            ('emp_info1', 'emp_info2'),
            ('emp_unit_code', 'emp_unit_deal'),
            ('emp_unit_name', 'emp_unit_hired'),
            'emp_unit_type',
            'emp_unit_industry',
            'emp_unit_loc',
            'emp_unit_jobtype',
            ('emp_unit_phone', 'emp_unit_communicate'),
            'emp_stu_sendmethod',
            ('emp_stu_phone', 'emp_stu_qq'),
            ('emp_stu_email', 'emp_stu_homephone'),
        ),
    }],
)
EmploymentInlineFieldSets = (
    [None, {
        'fields': (
            'emp_type',
            'emp_direction',
            'emp_sign_type',
            'emp_sign_unit',
            'emp_sign_loc',
            ('emp_file_unit', 'emp_file_phone'),
            ('emp_file_loc', 'emp_file_postcode'),
            ('emp_info1', 'emp_info2'),
            ('emp_unit_code', 'emp_unit_deal'),
            ('emp_unit_name', 'emp_unit_hired'),
            'emp_unit_type',
            'emp_unit_industry',
            'emp_unit_loc',
            'emp_unit_jobtype',
            ('emp_unit_phone', 'emp_unit_communicate'),
            'emp_stu_sendmethod',
            ('emp_stu_phone', 'emp_stu_qq'),
            ('emp_stu_email', 'emp_stu_homephone'),
        ),
    }],
)
StudentFieldSets = (
    [None, {
        'fields': (
            ('stu_id', 'stu_name', 'stu_gender'),
            ('stu_college', 'stu_class'),
            'stu_major',
            'stu_tutor',
            'stu_birth',
            'stu_identity',
            'stu_political_status',
            'stu_folk',
            'stu_tel',
            'stu_graduate',
            'stu_location',
            'stu_direction',
        ),
    }],
)

PovertyFieldSets = (
    [None,{
        'fields':(

            ('por_id','por_stu'),
            'por_tel',
            ('por_family1','por_family1_tel'),
            'por_family1_job',
            ('por_family2','por_family2_tel'),
            'por_family2_job',
            'por_is_archived',
            'por_info',
        ),
    }],
)

PovertyInlineFieldSets = (
    [None, {
        'fields': (
            'por_tel',
            ('por_family1', 'por_family1_tel'),
            'por_family1_job',
            ('por_family2', 'por_family2_tel'),
            'por_family2_job',
            'por_is_archived',
            'por_info',
        )
    }],
)