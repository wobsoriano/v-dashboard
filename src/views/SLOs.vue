<template>
  <div>
    <h3 class="text-gray-700 text-3xl font-medium">Service Level Objectives</h3>

    <!-- SLO info cards -->
    <div class="mt-4">
      <div class="flex flex-wrap -mx-6">
        <Card title="Services" iconColor="bg-indigo-600">
          <svg
            class="h-8 w-8 text-white"
            viewBox="0 0 28 30"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M18.2 9.08889C18.2 11.5373 16.3196 13.5222 14 13.5222C11.6804 13.5222 9.79999 11.5373 9.79999 9.08889C9.79999 6.64043 11.6804 4.65556 14 4.65556C16.3196 4.65556 18.2 6.64043 18.2 9.08889Z"
              fill="currentColor"
            />
            <path
              d="M25.2 12.0444C25.2 13.6768 23.9464 15 22.4 15C20.8536 15 19.6 13.6768 19.6 12.0444C19.6 10.4121 20.8536 9.08889 22.4 9.08889C23.9464 9.08889 25.2 10.4121 25.2 12.0444Z"
              fill="currentColor"
            />
            <path
              d="M19.6 22.3889C19.6 19.1243 17.0927 16.4778 14 16.4778C10.9072 16.4778 8.39999 19.1243 8.39999 22.3889V26.8222H19.6V22.3889Z"
              fill="currentColor"
            />
            <path
              d="M8.39999 12.0444C8.39999 13.6768 7.14639 15 5.59999 15C4.05359 15 2.79999 13.6768 2.79999 12.0444C2.79999 10.4121 4.05359 9.08889 5.59999 9.08889C7.14639 9.08889 8.39999 10.4121 8.39999 12.0444Z"
              fill="currentColor"
            />
            <path
              d="M22.4 26.8222V22.3889C22.4 20.8312 22.0195 19.3671 21.351 18.0949C21.6863 18.0039 22.0378 17.9556 22.4 17.9556C24.7197 17.9556 26.6 19.9404 26.6 22.3889V26.8222H22.4Z"
              fill="currentColor"
            />
            <path
              d="M6.64896 18.0949C5.98058 19.3671 5.59999 20.8312 5.59999 22.3889V26.8222H1.39999V22.3889C1.39999 19.9404 3.2804 17.9556 5.59999 17.9556C5.96219 17.9556 6.31367 18.0039 6.64896 18.0949Z"
              fill="currentColor"
            />
          </svg>
        </Card>

        <Card title="SLOs" iconColor="bg-orange-600">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 26"
            stroke="currentColor"
            class="h-8 w-8 text-white"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
            />
          </svg>
        </Card>
        <Card title="Alerts" iconColor="bg-pink-600">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 26"
            class="h-8 w-8 text-white"
          >
            <path
              d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
              fill="currentColor"
              stroke="currentColor"
              stroke-width="2"
              stroke-linejoin="round"
            />
          </svg>
        </Card>
      </div>
    </div>

    <!-- "Last 24 Hours" section -->
    <div class="text-lg text-gray-600">
      <!-- Roller header -->
      <div
        class="px-5 py-3 my-2 flex items-center shadow-md rounded-lg bg-gray-900"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 22 22"
          class="h-8 w-8"
          stroke="white"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>

        <span class="px-5 uppercase font-semibold text-gray-300">
          Last 24 hours
        </span>

        <svg
          v-if="!toggleLast24Hours"
          v-on:click="toggleLast24Hours = !toggleLast24Hours"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 22 22"
          class="h-6 w-6"
          stroke="white"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          />
        </svg>
        <svg
          v-if="toggleLast24Hours"
          v-on:click="toggleLast24Hours = !toggleLast24Hours"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 22 22"
          class="h-6 w-6"
          stroke="white"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M20 12H4"
          />
        </svg>
      </div>

      <!-- SLO Data Table-->
      <div
        class="-mx-4 sm:-mx-8 px-4 sm:px-8 overflow-x-auto fluid"
        :class="toggleLast24Hours ? '' : 'hidden'"
      >
        <!-- Filters -->
        <div class="flex flex-wrap gap-1 pb-2">
          <!-- Add filter input -->
          <div class="flex flex-wrap gap-1">
            <div class="justify-center relative text-gray-500">
              <!-- Input box -->
              <div
                class="px-2 py-2 flex items-center text-sm text-gray-200 bg-gray-900 rounded-full"
              >
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 22 22"
                  class="h-4 w-4"
                  stroke="white"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M12 6v6m0 0v6m0-6h6m-6 0H6"
                  />
                </svg>
                <input
                  v-model="input"
                  class="pl-2 border border-transparent bg-gray-900 text-gray-200 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                  placeholder="Add filter ..."
                />
              </div>

              <!-- Context menu for filter keys -->
              <div class="text-gray-500 text-xs text-semibold">
                <ul class="px-5 absolute">
                  <li
                    v-on:click="
                      enableFilterKey = false;
                      filterKeyResponse = [];
                      input = choice;
                    "
                    v-for="choice in filterKeyResponse"
                    :key="choice"
                    class="px-2 py-2 bg-gray-900 cursor-pointer border-t-2 border-gray-800 hover:bg-yellow-50 hover:text-red-500"
                  >
                    {{ choice }}
                  </li>
                </ul>

                <!-- Context menu for filter values -->
                <ul class="px-5 absolute">
                  <li
                    v-on:click="
                      params[input] = choice;
                      filterValueResponse = [];
                      input = '';
                      enableFilterKey = true;
                    "
                    v-for="choice in filterValueResponse"
                    :key="choice"
                    class="px-2 py-2 bg-gray-900 cursor-pointer border-t-2 border-gray-800 hover:bg-yellow-50 hover:text-red-500"
                  >
                    {{ choice }}
                  </li>
                </ul>
              </div>
            </div>
          </div>

          <!-- Active filters -->
          <div class="flex flex-wrap gap-1 pb-2">
            <div
              class="px-2 py-2 flex items-center text-sm text-gray-200 bg-gray-900 rounded-full"
              v-for="(value, index) in params"
              :key="index"
            >
              <span class="px-1 font-semibold">{{ index }}:</span>
              <span class="pr-1">{{ value }}</span>
              <svg
                v-on:click="delete params[index]"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="red"
                class="h-4 w-4"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </div>
          </div>
        </div>

        <!-- Table -->
        <div
          class="inline-block min-w-full shadow rounded-lg overflow-hidden bg-gray-800"
        >
          <table class="min-w-max w-full table-auto">
            <!-- Table headers -->
            <thead>
              <tr
                class="bg-gray-900 text-gray-200 uppercase text-sm leading-normal"
              >
                <th class="px-2 py-4 text-left"></th>
                <th class="px-2 py-4 text-left">Description</th>
                <th class="px-2 py-4 text-left">Measurement</th>
                <th class="px-2 py-4 text-left">Name</th>
                <th class="px-2 py-4 text-left">Window</th>
                <th class="px-2 py-4 text-left">Metadata</th>
                <th class="px-2 py-4 text-left">Actions</th>
              </tr>
            </thead>

            <!-- Table body -->
            <tbody class="text-gray-200 text-sm font-light">
              <Loader :loading="loading" text="Loading data ..."/>

              <!-- Rows -->
              <tr
                v-for="(i, index) in sloData"
                :key="index"
                class="border-b border-gray-600 bg-gray-800 hover:bg-gray-70"
              >
                <!-- Warning / Check -->
                <td class="px-4">
                  <StatusIcon :alert="i.alert" />
                </td>

                <!-- SLO Description -->
                <td class="px-2 text-left font-semibold max-w-xs">
                  {{ i.slo_description }}
                </td>

                <!-- SLO -->
                <td class="px-2">
                  <SLOCard
                    class="grid grid-cols-1 xl:grid-cols-2 gap-1"
                    :sli="i.sli_measurement"
                    :slo="i.slo_target"
                    :gap="i.gap"
                    :good_events="i.good_events_count"
                    :bad_events="i.bad_events_count"
                    :burn_rate="i.error_budget_burn_rate"
                    :burn_rate_threshold="i.alerting_burn_rate_threshold"
                  />
                </td>

                <!-- SLO Name -->
                <td class="px-2 text-left whitespace-pre max-w-xs">
                  <div class="text-md flex items-center">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                      class="h-4 w-4 mr-1"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M9 17v-2m3 2v-4m3 4v-6m2 10H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                      />
                    </svg>
                    <div v-on:click="params['slo_name'] = i.slo_name">
                      {{ i.slo_name }}
                    </div>
                  </div>
                </td>

                <!-- Window -->
                <td class="px-2 text-left max-w-xs whitespace-pre">
                  <div
                    v-on:click="params['window'] = fmtTime(i.window)"
                    class="text-md flex items-center"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 22 22"
                      class="h-4 w-4 mr-1"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                      />
                    </svg>
                    <div>
                      {{ fmtTime(i.window) }}
                    </div>
                  </div>
                </td>

                <!-- Metadata labels -->
                <td class="px-2 py-4 text-xs max-w-xs">
                  <div class="flex flex-wrap gap-2">
                    <div
                      v-on:click="params['service_name'] = i.service_name"
                      class="px-1 py-1 flex items-center text-gray-200 bg-gray-500 bg-opacity-25 rounded-full"
                    >
                      <span class="px-1 font-semibold">service:</span>
                      <span class="pr-1">{{ i.service_name }}</span>
                    </div>
                    <div
                      v-on:click="params['feature_name'] = i.feature_name"
                      class="px-1 py-1 flex items-center text-gray-200 bg-gray-500 bg-opacity-25 rounded-full"
                    >
                      <span class="px-1 font-semibold">feature:</span>
                      <span class="pr-1">{{ i.feature_name }}</span>
                    </div>
                    <div
                      class="px-1 py-1 flex items-center text-gray-200 bg-gray-500 bg-opacity-25 rounded-full"
                      v-for="(element, index) in JSON.parse(i.metadata)"
                      :key="index"
                      v-on:click="
                        params['metadata.' + element.key] = element.value
                      "
                    >
                      <span class="px-1 font-semibold">{{ element.key }}:</span>
                      <span class="pr-1">{{ element.value }}</span>
                    </div>
                  </div>
                </td>

                <!-- Actions -->
                <td class="px-2 text-xs">
                  <div class="flex item-center justify-center">
                    <!-- View icon -->
                    <div
                      class="w-4 mr-2 transform hover:text-purple-500 hover:scale-110"
                    >
                      <svg
                        v-on:click="navigateSLO(i, 'view')"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                        ></path>
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                        ></path>
                      </svg>
                    </div>

                    <!-- Edit icon -->
                    <div
                      class="w-4 mr-2 transform hover:text-purple-500 hover:scale-110"
                    >
                      <svg
                        v-on:click="navigateSLO(i, 'edit')"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
                        ></path>
                      </svg>
                    </div>

                    <!-- Remove icon -->
                    <div
                      class="w-4 mr-2 transform hover:text-purple-500 hover:scale-110"
                    >
                      <svg
                        v-on:click="navigateSLO(i, 'remove')"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
                        ></path>
                      </svg>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>

          <!-- Table footer -->
          <div
            v-if="!loading"
            class="px-5 py-5 bg-gray-800 text-gray-200 flex flex-col xs:flex-row items-center xs:justify-between"
          >
            <!-- Table footer text -->
            <span v-if="count < offset + limit" class="text-xs xs:text-sm">
              Showing query results {{ offset + 1 }} to
              {{ offset + sloData.length }}
            </span>
            <span v-else class="text-xs xs:text-sm">
              Showing query results {{ offset + 1 }} to
              {{ offset + sloData.length }}
            </span>

            <!-- Footer buttons -->
            <div class="inline-flex mt-2 xs:mt-0">
              <!-- Previous button -->
              <button
                v-if="offset > 0"
                v-on:click="
                  offset -= limit;
                  reloadData();
                "
                class="text-sm bg-gray-800 hover:bg-gray-600 border font-semibold px-4 rounded-full"
              >
                Previous
              </button>

              <!-- Next button -->
              <button
                v-else
                v-on:click="
                  offset += limit;
                  reloadData();
                "
                class="text-sm bg-gray-800 hover:bg-gray-600 border font-semibold py-2 px-4 rounded-full"
              >
                Next
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- New SLO button -->
    <div>
      <button
        class="px-2 py-2 bg-blue-600 rounded-md text-white font-medium tracking-wide hover:bg-blue-500 inline-flex items-center"
      >
        <svg
          class="fill-current w-4 h-4 mr-2"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="3"
            d="M12 6v6m0 0v6m0-6h6m-6 0H6"
          />
        </svg>
        <span>New SLO</span>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { slos } from "../hooks/api";
import { sloMixin, fmtMixin, queryMixin } from "../hooks/shared";
import SLOCard from "../components/SLOCard.vue";
import Card from "../components/Card.vue";
import Loader from "../components/Loader.vue";
import StatusIcon from "../components/icons/StatusIcon.vue";

export default defineComponent({
  data() {
    return {
      sloData: [],
      offset: 0,
      count: 0,
      limit: 50,
      loading: true,
      toggleLast24Hours: true,
      params: {},
      input: "",
      enableFilterKey: true,
      filterKeyResponse: [],
      filterValueResponse: [],
      columns: [],
    };
  },
  mounted() {
    this.params = this.$route.query;
    this.reloadData();
    slos.getLastReportCount()
      .then((resJson) => this.count = resJson[0].count)
  },
  watch: {
    params: {
      handler() {
        console.log("Watcher triggered");
        this.updateQueryString();
        this.reloadData();
      },
      deep: true,
    },
    input: function (query) {
      if (query == "") {
        this.enableFilterKey = true;
        return;
      }
      if (this.enableFilterKey) {
        slos.getKeys(query).then((resJson) => {
          this.filterKeyResponse = resJson;
        })
      } else {
        slos.getValues(query).then((resJson) => {
          this.filterValueResponse = resJson;
        })
      }
    },
  },
  methods: {
    async reloadData() {
      this.sloData = [];
      this.loading = true;
      var queryString = this.getQueryString();
      slos.getLastReport(queryString, this.offset, this.limit)
        .then((resJson) => {
          this.sloData = resJson;
          this.loading = false;
        })
    },
    async getSloCount() {
      slos.getLastReportCount().then((resJson => this.count = resJson[0].count))
    },
  },
  mixins: [fmtMixin, sloMixin, queryMixin],
  components: {
    Card,
    SLOCard,
    StatusIcon,
    Loader
  },
});
</script>
