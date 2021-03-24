export const queryMixin = {
    methods: {
      getQueryString(): string {
        return Object.keys(this.params)
          .map((key) => key + "=" + this.params[key])
          .join("&");
      },
      updateQueryString() {
        console.log("Within router");
        history.pushState(
          {},
          "",
          this.$route.path + "?" + this.getQueryString()
        );
      }
    }
}

export const fmtMixin = {
  methods: {
    fmtFloat(n: number, digits: number){
      return parseFloat(n.toFixed(digits))
    },
    fmtTime(seconds: number) {
      var days = Math.floor(seconds / (24 * 60 * 60));
      seconds -= days * (24 * 60 * 60);
      var hours = Math.floor(seconds / (60 * 60));
      seconds -= hours * (60 * 60);
      var minutes = Math.floor(seconds / 60);
      seconds -= minutes * 60;
      var dDisplay = days > 0 ? days + "d" : "";
      var hDisplay = hours > 0 ? hours + "h" : "";
      var mDisplay = minutes > 0 ? minutes + "m" : "";
      var sDisplay = seconds > 0 ? seconds + "s" : "";
      return dDisplay + hDisplay + mDisplay + sDisplay;
    },
    fmtAmount(n: number) {
      var nDisplay = "";
      if (n == -1) {
        return "N/A";
      }
      if (n >= 1000000000) {
        n /= 1000000000;
        nDisplay = n.toFixed(0) + "B";
      } else if (n >= 1000000) {
        n /= 1000000;
        nDisplay = n.toFixed(0) + "M";
      } else if (n >= 1000) {
        n /= 1000;
        nDisplay = n.toFixed(0) + "k";
      } else {
        nDisplay = String(n);
      }
      return nDisplay;
    },
    snakeToCamel(str: string) {
      return str.replace(/([-_][a-z])/g, (group) =>
        group.toUpperCase().replace("-", "").replace("_", "")
      );
    },
  }
}

export const sloMixin = {
  methods: {
    navigateSLO(data: Object, method: string) {
      var name = this.getSLOName(data);
      this.$router.push({ path: `/slo/${name}/${method}` });
    },
    getSLOName(data: Object) {
      return (data as any).service_name + "-" + (data as any).feature_name + "-" + (data as any).slo_name;
    },
  },
}
