/*!
 * jQuery Form Plugin
 * version: 2.69 (06-APR-2011)
 * @requires jQuery v1.3.2 or later
 *
 * Examples and documentation at: http://malsup.com/jquery/form/
 * Dual licensed under the MIT and GPL licenses:
 *   http://www.opensource.org/licenses/mit-license.php
 *   http://www.gnu.org/licenses/gpl.html
 */
(function (a) {
  function b() {
    if (a.fn.ajaxSubmit.debug) {
      var b = "[jquery.form] " + Array.prototype.join.call(arguments, "");
      window.console && window.console.log
        ? window.console.log(b)
        : window.opera && window.opera.postError && window.opera.postError(b);
    }
  }
  (a.fn.ajaxSubmit = function (c) {
    function r() {
      function t() {
        if (!j.aborted) {
          var c = i.contentWindow
            ? i.contentWindow.document
            : i.contentDocument
            ? i.contentDocument
            : i.document;
          if (!c || c.location.href == e.iframeSrc) if (!m) return;
          i.detachEvent
            ? i.detachEvent("onload", t)
            : i.removeEventListener("load", t, !1);
          var d = !0;
          try {
            if (m) throw "timeout";
            var f = e.dataType == "xml" || c.XMLDocument || a.isXMLDoc(c);
            b("isXml=" + f);
            if (
              !f &&
              window.opera &&
              (c.body == null || c.body.innerHTML == "") &&
              --s
            ) {
              b("requeing onLoad callback, DOM not available"),
                setTimeout(t, 250);
              return;
            }
            (j.responseText = c.body
              ? c.body.innerHTML
              : c.documentElement
              ? c.documentElement.innerHTML
              : null),
              (j.responseXML = c.XMLDocument ? c.XMLDocument : c),
              (j.getResponseHeader = function (a) {
                var b = { "content-type": e.dataType };
                return b[a];
              });
            var g = /(json|script)/.test(e.dataType);
            if (g || e.textarea) {
              var l = c.getElementsByTagName("textarea")[0];
              if (l) j.responseText = l.value;
              else if (g) {
                var n = c.getElementsByTagName("pre")[0],
                  o = c.getElementsByTagName("body")[0];
                n
                  ? (j.responseText = n.textContent)
                  : o && (j.responseText = o.innerHTML);
              }
            } else
              e.dataType == "xml" &&
                !j.responseXML &&
                j.responseText != null &&
                (j.responseXML = u(j.responseText));
            q = w(j, e.dataType, e);
          } catch (p) {
            b("error caught:", p),
              (d = !1),
              (j.error = p),
              e.error && e.error.call(e.context, j, "error", p),
              k && a.event.trigger("ajaxError", [j, e, p]);
          }
          j.aborted && (b("upload aborted"), (d = !1)),
            d &&
              (e.success && e.success.call(e.context, q, "success", j),
              k && a.event.trigger("ajaxSuccess", [j, e])),
            k && a.event.trigger("ajaxComplete", [j, e]),
            k && !--a.active && a.event.trigger("ajaxStop"),
            e.complete &&
              e.complete.call(e.context, j, d ? "success" : "error"),
            setTimeout(function () {
              h.removeData("form-plugin-onload"),
                h.remove(),
                (j.responseXML = null);
            }, 100);
        }
      }
      function p() {
        var b = l.attr("target"),
          c = l.attr("action");
        d.setAttribute("target", f),
          d.getAttribute("method") != "POST" &&
            d.setAttribute("method", "POST"),
          d.getAttribute("action") != e.url && d.setAttribute("action", e.url),
          e.skipEncodingOverride ||
            l.attr({
              encoding: "multipart/form-data",
              enctype: "multipart/form-data",
            }),
          e.timeout &&
            setTimeout(function () {
              (m = !0), t();
            }, e.timeout);
        var g = [];
        try {
          if (e.extraData)
            for (var j in e.extraData)
              g.push(
                a(
                  '<input type="hidden" name="' +
                    j +
                    '" value="' +
                    e.extraData[j] +
                    '" />'
                ).appendTo(d)[0]
              );
          h.appendTo("body"),
            i.attachEvent
              ? i.attachEvent("onload", t)
              : i.addEventListener("load", t, !1),
            d.submit();
        } finally {
          d.setAttribute("action", c),
            b ? d.setAttribute("target", b) : l.removeAttr("target"),
            a(g).remove();
        }
      }
      var d = l[0];
      if (a(":input[name=submit],:input[id=submit]", d).length)
        alert('Error: Form elements must not have name or id of "submit".');
      else {
        var e = a.extend(!0, {}, a.ajaxSettings, c);
        e.context = e.context || e;
        var f = "jqFormIO" + new Date().getTime(),
          g = "_" + f,
          h = a(
            '<iframe id="' +
              f +
              '" name="' +
              f +
              '" src="' +
              e.iframeSrc +
              '" />'
          ),
          i = h[0];
        h.css({ position: "absolute", top: "-1000px", left: "-1000px" });
        var j = {
            aborted: 0,
            responseText: null,
            responseXML: null,
            status: 0,
            statusText: "n/a",
            getAllResponseHeaders: function () {},
            getResponseHeader: function () {},
            setRequestHeader: function () {},
            abort: function () {
              b("aborting upload...");
              var c = "aborted";
              (this.aborted = 1),
                h.attr("src", e.iframeSrc),
                (j.error = c),
                e.error && e.error.call(e.context, j, "error", c),
                k && a.event.trigger("ajaxError", [j, e, c]),
                e.complete && e.complete.call(e.context, j, "error");
            },
          },
          k = e.global;
        k && !a.active++ && a.event.trigger("ajaxStart"),
          k && a.event.trigger("ajaxSend", [j, e]);
        if (e.beforeSend && e.beforeSend.call(e.context, j, e) === !1) {
          e.global && a.active--;
          return;
        }
        if (j.aborted) return;
        var m = 0,
          n = d.clk;
        if (n) {
          var o = n.name;
          o &&
            !n.disabled &&
            ((e.extraData = e.extraData || {}),
            (e.extraData[o] = n.value),
            n.type == "image" &&
              ((e.extraData[o + ".x"] = d.clk_x),
              (e.extraData[o + ".y"] = d.clk_y)));
        }
        e.forceSync ? p() : setTimeout(p, 10);
        var q,
          r,
          s = 50,
          u =
            a.parseXML ||
            function (a, b) {
              window.ActiveXObject
                ? ((b = new ActiveXObject("Microsoft.XMLDOM")),
                  (b.async = "false"),
                  b.loadXML(a))
                : (b = new DOMParser().parseFromString(a, "text/xml"));
              return b &&
                b.documentElement &&
                b.documentElement.nodeName != "parsererror"
                ? b
                : null;
            },
          v =
            a.parseJSON ||
            function (a) {
              return window.eval("(" + a + ")");
            },
          w = function (b, c, d) {
            var e = b.getResponseHeader("content-type") || "",
              f = c === "xml" || (!c && e.indexOf("xml") >= 0),
              g = f ? b.responseXML : b.responseText;
            f &&
              g.documentElement.nodeName === "parsererror" &&
              a.error &&
              a.error("parsererror"),
              d && d.dataFilter && (g = d.dataFilter(g, c)),
              typeof g == "string" &&
                (c === "json" || (!c && e.indexOf("json") >= 0)
                  ? (g = v(g))
                  : (c === "script" || (!c && e.indexOf("javascript") >= 0)) &&
                    a.globalEval(g));
            return g;
          };
      }
    }
    if (!this.length) {
      b("ajaxSubmit: skipping submit process - no element selected");
      return this;
    }
    typeof c == "function" && (c = { success: c });
    var d = this.attr("action"),
      e = typeof d == "string" ? a.trim(d) : "";
    e && (e = (e.match(/^([^#]+)/) || [])[1]),
      (e = e || window.location.href || ""),
      (c = a.extend(
        !0,
        {
          url: e,
          success: a.ajaxSettings.success,
          type: this[0].getAttribute("method") || "GET",
          iframeSrc: /^https/i.test(window.location.href || "")
            ? "javascript:false"
            : "about:blank",
        },
        c
      ));
    var f = {};
    this.trigger("form-pre-serialize", [this, c, f]);
    if (f.veto) {
      b("ajaxSubmit: submit vetoed via form-pre-serialize trigger");
      return this;
    }
    if (c.beforeSerialize && c.beforeSerialize(this, c) === !1) {
      b("ajaxSubmit: submit aborted via beforeSerialize callback");
      return this;
    }
    var g,
      h,
      i = this.formToArray(c.semantic);
    if (c.data) {
      c.extraData = c.data;
      for (g in c.data)
        if (c.data[g] instanceof Array)
          for (var j in c.data[g]) i.push({ name: g, value: c.data[g][j] });
        else
          (h = c.data[g]),
            (h = a.isFunction(h) ? h() : h),
            i.push({ name: g, value: h });
    }
    if (c.beforeSubmit && c.beforeSubmit(i, this, c) === !1) {
      b("ajaxSubmit: submit aborted via beforeSubmit callback");
      return this;
    }
    this.trigger("form-submit-validate", [i, this, c, f]);
    if (f.veto) {
      b("ajaxSubmit: submit vetoed via form-submit-validate trigger");
      return this;
    }
    var k = a.param(i);
    c.type.toUpperCase() == "GET"
      ? ((c.url += (c.url.indexOf("?") >= 0 ? "&" : "?") + k), (c.data = null))
      : (c.data = k);
    var l = this,
      m = [];
    c.resetForm &&
      m.push(function () {
        l.resetForm();
      }),
      c.clearForm &&
        m.push(function () {
          l.clearForm();
        });
    if (!c.dataType && c.target) {
      var n = c.success || function () {};
      m.push(function (b) {
        var d = c.replaceTarget ? "replaceWith" : "html";
        a(c.target)[d](b).each(n, arguments);
      });
    } else c.success && m.push(c.success);
    c.success = function (a, b, d) {
      var e = c.context || c;
      for (var f = 0, g = m.length; f < g; f++)
        m[f].apply(e, [a, b, d || l, l]);
    };
    var o = a("input:file", this).length > 0,
      p = "multipart/form-data",
      q = l.attr("enctype") == p || l.attr("encoding") == p;
    c.iframe !== !1 && (o || c.iframe || q)
      ? c.closeKeepAlive
        ? a.get(c.closeKeepAlive, r)
        : r()
      : a.ajax(c),
      this.trigger("form-submit-notify", [this, c]);
    return this;
  }),
    (a.fn.ajaxForm = function (c) {
      if (this.length === 0) {
        var d = { s: this.selector, c: this.context };
        if (!a.isReady && d.s) {
          b("DOM not ready, queuing ajaxForm"),
            a(function () {
              a(d.s, d.c).ajaxForm(c);
            });
          return this;
        }
        b(
          "terminating; zero elements found by selector" +
            (a.isReady ? "" : " (DOM not ready)")
        );
        return this;
      }
      return this.ajaxFormUnbind()
        .bind("submit.form-plugin", function (b) {
          b.isDefaultPrevented() || (b.preventDefault(), a(this).ajaxSubmit(c));
        })
        .bind("click.form-plugin", function (b) {
          var c = b.target,
            d = a(c);
          if (!d.is(":submit,input:image")) {
            var e = d.closest(":submit");
            if (e.length == 0) return;
            c = e[0];
          }
          var f = this;
          f.clk = c;
          if (c.type == "image")
            if (b.offsetX != undefined)
              (f.clk_x = b.offsetX), (f.clk_y = b.offsetY);
            else if (typeof a.fn.offset == "function") {
              var g = d.offset();
              (f.clk_x = b.pageX - g.left), (f.clk_y = b.pageY - g.top);
            } else
              (f.clk_x = b.pageX - c.offsetLeft),
                (f.clk_y = b.pageY - c.offsetTop);
          setTimeout(function () {
            f.clk = f.clk_x = f.clk_y = null;
          }, 100);
        });
    }),
    (a.fn.ajaxFormUnbind = function () {
      return this.unbind("submit.form-plugin click.form-plugin");
    }),
    (a.fn.formToArray = function (b) {
      var c = [];
      if (this.length === 0) return c;
      var d = this[0],
        e = b ? d.getElementsByTagName("*") : d.elements;
      if (!e) return c;
      var f, g, h, i, j, k, l;
      for (f = 0, k = e.length; f < k; f++) {
        (j = e[f]), (h = j.name);
        if (!h) continue;
        if (b && d.clk && j.type == "image") {
          !j.disabled &&
            d.clk == j &&
            (c.push({ name: h, value: a(j).val() }),
            c.push(
              { name: h + ".x", value: d.clk_x },
              { name: h + ".y", value: d.clk_y }
            ));
          continue;
        }
        i = a.fieldValue(j, !0);
        if (i && i.constructor == Array)
          for (g = 0, l = i.length; g < l; g++)
            c.push({ name: h, value: i[g] });
        else
          i !== null &&
            typeof i != "undefined" &&
            c.push({ name: h, value: i });
      }
      if (!b && d.clk) {
        var m = a(d.clk),
          n = m[0];
        (h = n.name),
          h &&
            !n.disabled &&
            n.type == "image" &&
            (c.push({ name: h, value: m.val() }),
            c.push(
              { name: h + ".x", value: d.clk_x },
              { name: h + ".y", value: d.clk_y }
            ));
      }
      return c;
    }),
    (a.fn.formSerialize = function (b) {
      return a.param(this.formToArray(b));
    }),
    (a.fn.fieldSerialize = function (b) {
      var c = [];
      this.each(function () {
        var d = this.name;
        if (!!d) {
          var e = a.fieldValue(this, b);
          if (e && e.constructor == Array)
            for (var f = 0, g = e.length; f < g; f++)
              c.push({ name: d, value: e[f] });
          else
            e !== null &&
              typeof e != "undefined" &&
              c.push({ name: this.name, value: e });
        }
      });
      return a.param(c);
    }),
    (a.fn.fieldValue = function (b) {
      for (var c = [], d = 0, e = this.length; d < e; d++) {
        var f = this[d],
          g = a.fieldValue(f, b);
        if (
          g === null ||
          typeof g == "undefined" ||
          (g.constructor == Array && !g.length)
        )
          continue;
        g.constructor == Array ? a.merge(c, g) : c.push(g);
      }
      return c;
    }),
    (a.fieldValue = function (b, c) {
      var d = b.name,
        e = b.type,
        f = b.tagName.toLowerCase();
      c === undefined && (c = !0);
      if (
        c &&
        (!d ||
          b.disabled ||
          e == "reset" ||
          e == "button" ||
          ((e == "checkbox" || e == "radio") && !b.checked) ||
          ((e == "submit" || e == "image") && b.form && b.form.clk != b) ||
          (f == "select" && b.selectedIndex == -1))
      )
        return null;
      if (f == "select") {
        var g = b.selectedIndex;
        if (g < 0) return null;
        var h = [],
          i = b.options,
          j = e == "select-one",
          k = j ? g + 1 : i.length;
        for (var l = j ? g : 0; l < k; l++) {
          var m = i[l];
          if (m.selected) {
            var n = m.value;
            n ||
              (n =
                m.attributes &&
                m.attributes.value &&
                !m.attributes.value.specified
                  ? m.text
                  : m.value);
            if (j) return n;
            h.push(n);
          }
        }
        return h;
      }
      return a(b).val();
    }),
    (a.fn.clearForm = function () {
      return this.each(function () {
        a("input,select,textarea", this).clearFields();
      });
    }),
    (a.fn.clearFields = a.fn.clearInputs =
      function () {
        return this.each(function () {
          var a = this.type,
            b = this.tagName.toLowerCase();
          a == "text" || a == "password" || b == "textarea"
            ? (this.value = "")
            : a == "checkbox" || a == "radio"
            ? (this.checked = !1)
            : b == "select" && (this.selectedIndex = -1);
        });
      }),
    (a.fn.resetForm = function () {
      return this.each(function () {
        (typeof this.reset == "function" ||
          (typeof this.reset == "object" && !this.reset.nodeType)) &&
          this.reset();
      });
    }),
    (a.fn.enable = function (a) {
      a === undefined && (a = !0);
      return this.each(function () {
        this.disabled = !a;
      });
    }),
    (a.fn.selected = function (b) {
      b === undefined && (b = !0);
      return this.each(function () {
        var c = this.type;
        if (c == "checkbox" || c == "radio") this.checked = b;
        else if (this.tagName.toLowerCase() == "option") {
          var d = a(this).parent("select");
          b &&
            d[0] &&
            d[0].type == "select-one" &&
            d.find("option").selected(!1),
            (this.selected = b);
        }
      });
    });
})(jQuery);
