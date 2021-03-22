export const sloConfig = {
  async get(name: string) {
    return (await fetch(`/api/slo/${name}`)).json()
  },
  async update(name: string, data: Object) {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    }
    return (await fetch(`/api/slo/${name}`, requestOptions)).json()
  },
  async test(name: string) {
    return (await fetch(`/api/slo/${name}/test`)).json()
  },
  async diff(name: string) {
    return (await fetch(`/api/slo/${name}/diff`)).json()
  }
}

export const slos = {
  async getKeys(query: string) {
    return (await fetch(`/api/slos/keys?q=${query}`)).json()
  },
  async getValues(query: string) {
    return (await fetch(`/api/slos/values?q=${query}`)).json()
  },
  async getLastReportCount() {
    return (await fetch(`/api/slos/last_report_count`)).json()
  },
  async getLastReport(query: string, offset: number, limit: number) {
    return (await fetch(
      `/api/slos/last_report?offset=${offset}&limit=${limit}&${query}`
    )).json()
  }
}
