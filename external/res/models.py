import attr


@attr.s
class NYCResComplaint(object):
    created_date = attr.ib()
    incident_zip = attr.ib()
    incident_address = attr.ib()
    city = attr.ib()
    complaint_type = attr.ib()
    descriptor = attr.ib()
    status = attr.ib()