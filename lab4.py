#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

TAX_PROVINCIAL = 0.05
TAX_FEDERAL = 0.025
TAX_TOTAL = 0.075
PURCHASE_TOTAL = 1.075

#
# def provincial_tax(purchase):
#     provincial_tax = (purchase*0.05)
#     return provincial_tax()
#
#
# def federal_tax(purchase):
#     federal_tax = (purchase*0.025)
#     return federal_tax()
#
#
# def total(purchase):
#     result = purchase + provincial_tax(purchase) + federal_tax(purchase)
#     return result


def bill_of_sale(purchase):
    file_name = "sale.txt"
    with open(file_name, 'w') as output_file:
        output_file.write("Amount of purchase: {0:.2f}\n".format(purchase))
        output_file.write("Provincial tax: {0:.2f}\n".format(purchase * TAX_PROVINCIAL))
        output_file.write("Federal tax: {0:.2f}\n".format(purchase * TAX_FEDERAL))
        output_file.write("Total tax: {0:.2f}\n".format(purchase * TAX_TOTAL))
        output_file.write("Total sale: {0:.2f}\n".format(purchase * PURCHASE_TOTAL))

bill_of_sale(10)