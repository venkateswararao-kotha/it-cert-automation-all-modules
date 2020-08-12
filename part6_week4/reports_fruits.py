#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import locale
import sys
import os
from collections import defaultdict
#import reports
#import emails

def get_date():
    x = datetime.datetime.now()
    return x.strftime("%b %d, %Y")

def fruits_summary_dict_data():
  dirpath = '~/supplier-data/images'
  files = [f for f in os.listdir(dirpath)
             if os.path.isfile(os.path.join(dirpath, f))]
  print(files)
  os.chdir("~/supplier-data/images")
  for file in files:
    fruits_summary_dict = dict()
    with open(file,'r') as f:
      name = next(f).strip('\n')
      weight = int(next(f).strip('\n').split()[0])
      description = next(f).strip('\n')

      if fruits_summary_dict[name]:
        fruits_summary_dict[name] += weight
      else:
        fruits_summary_dict[name] = weight
  return fruits_summary_dict


def fruits_dict_to_table(fruits_summary_dict):
  """Turns the data in car_data into a list of lists."""
  for key, value in fruits_summary_dict.items():
    fruit_name = "name: {}".format(key)
    fruit_weight = "weight: {} lbs".format(value)

    table_data.append(fruit_name)
    table_data.append(fruit_weight)
    table_data.append('<br/>')
  return table_data


def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  #report.build([report_title, empty_line, report_info, empty_line, report_table])
  report.build([report_title, empty_line, report_info, empty_line, report_table])


def main(argv):
  summary =  "Processed update on {} ".format(get_date())
  fruits_sum_dict_data = fruits_summary_dict_data()
  print(summary)
  report_table = fruits_dict_to_table(fruits_sum_dict_data)
  generate('/tmp/fruits_summary.pdf', "fruits report", summary, report_table)

  # TODO: send the PDF report as an email attachment
  #sender = "automation@example.com"
  #receiver = "{}@example.com".format(os.environ.get('USER'))
  #subject = "Sales summary for last month"

  #message = emails.generate(sender, receiver, subject, summary, "/tmp/fruits_summary.pdf")
  #emails.send(message



if __name__ == "__main__":
  main(sys.argv)

