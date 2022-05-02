from datetime import date, timedelta

def sqlite_insert(conn, table, df):
    for index, row in df.iterrows():
        cols = ', '.join('"{}"'.format(col) for col in df.columns)
        vals = ', '.join('{}'.format(val) for val in row)
        sql = 'INSERT INTO "{0}" ({1}) VALUES ({2})'.format(table, cols, vals)
        print(sql)
        conn.cursor().execute(sql, row)
        conn.commit()

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)