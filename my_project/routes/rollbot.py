from cProfile import label
from collections import defaultdict
from my_project import app
from flask import render_template, jsonify, request
from flask import request

from datetime import datetime, timedelta


@app.route("/v1_return", methods=["GET", "POST"])
def v1_return():

    def easyReturnCalc(share_value):
        yearly_rlb_gain = (share_value / 100) * 60 * 543
        dollar_worth = yearly_rlb_gain * 0.0022

        return yearly_rlb_gain,dollar_worth

    def complicatedReturnCalc():
        return

    if request.method == "POST":

        lotto_shares = request.form.get('rlb_share_value') or 100

        calcResult = easyReturnCalc(int(lotto_shares))

        return render_template("v1_return-result.html",pagetitle="V1 Return", lotto_shares=lotto_shares, calcResult=calcResult)

    return render_template("v1_return.html",pagetitle="V1 Return")