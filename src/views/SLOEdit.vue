<template>
  <div>
    <h3 class="mb-4 text-gray-700 font-medium text-3xl">SLO Configuration</h3>
    <SLOForm :data="data" @saved="saveConfig()" @reset="resetConfig()">
      <template v-slot:header>
        <div class="mb-2 m-2 text-right font-bold text-indigo-600">
          {{ data._relpath }}
        </div>
      </template>
      <template v-slot:buttons>
        <button
          @click="testConfig()"
          class="bg-indigo-500 hover:bg-indigo-800 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transform hover:scale-110 motion-reduce:transform-none"
        >
          Test
        </button>
      </template>

      <!-- Footer -->
      <template v-slot:footer>
        <div class="text-green-500" v-if="formSavedOnDisk">
          All changes saved to disk.
        </div>
        <div class="text-red-600" v-else-if="!formSavedSuccess">
          {{ formSavedError }}
        </div>
        <div class="text-orange-600" v-else>
          There are some unsaved changes.
        </div>

        <div class="text-green-500" v-if="configTestLoading">
          Validating config ...
        </div>

        <div class="text-green-500" v-if="configTestSuccess">
          {{ configTestSuccessMessage }}

          <div v-if="configTestData.length" class="pt-5 pb-5 text-gray-500 text-xl">Test results</div>
          <div class="flex" v-for="step in configTestData" :key="step.name">
            <div>{{ fmtTime(step.window) }}</div>
            <SLOCard
              class="flex"
              :sli="step.sli_measurement"
              :slo="step.slo_target"
              :gap="step.gap"
              :good_events="step.good_events_count"
              :bad_events="step.bad_events_count"
              :burn_rate="step.error_budget_burn_rate"
              :burn_rate_threshold="step.alerting_burn_rate_threshold"
            />
          </div>
        </div>
        <div class="text-red-600" v-else>
          {{ configTestErrorMessage }}
          <div class="text-gray-500 text-xl">Full traceback</div>
          <textarea
            rows=10
            class="resize bshadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            disabled
            v-model="configTestTraceback"
          />
        </div>
      </template>
    </SLOForm>

    <!-- Git diff -->
    <div v-if="sloGitDiff != ''">
      <h4 class="text-gray-700 text-3xl font-medium">Git diff</h4>
      <div class="mt-5 p-5 bg-white shadow-md rounded">
        <div v-for="line in sloGitDiff.split('<br>')" :key="line">
          <div
            v-if="line.startsWith('-')"
            class="bg-red-300"
            v-html="line"
          ></div>
          <div
            v-else-if="line.startsWith('+')"
            class="bg-green-200"
            v-html="line"
          ></div>
          <div v-else v-html="line"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
import { sloConfig } from "../hooks/api";
import { fmtMixin } from "../hooks/shared";
import SLOCard from "../components/SLOCard.vue";
import SLOForm from "../components/SLOForm.vue";

export default defineComponent({
  data() {
    return {
      name: this.$route.params.name,
      data: {},
      firstPageLoad: true,
      formSavedSuccess: true,
      formSavedOnDisk: true,
      formSavedError: "",
      sloGitDiff: "",
      configTestLoading: false,
      configTestSuccess: true,
      configTestErrorMessage: "",
      configTestSuccessMessage: "",
      configTestTraceback: "",
      configTestData: {},
    };
  },
  mounted() {
    this.firstPageLoad = true;
    sloConfig.get(this.name).then((resJson) => {
      this.data = resJson
    });
    this.fetchGitDiff()
  },
  watch: {
    data: {
      handler(val) {
        this.formSavedError = "";
        if (!this.firstPageLoad) {
          this.formSavedOnDisk = false
        }
        this.firstPageLoad = false
      },
      deep: true,
    },
  },
  methods: {
    async saveConfig() {
      this.configTestErrorMessage = ""
      this.configTestTraceback = ""
      this.configTestLoading = true
      sloConfig.update(this.name, this.data).then((resJson) => {
        this.configTested = false;
        this.configTestErrorMessage = ""
        if (resJson.success) {
          this.formSavedOnDisk = true
          this.formSavedSuccess = true
          this.fetchGitDiff()
          this.testConfig()
        } else {
          this.formSavedOnDisk = false
          this.formSavedSuccess = false
          this.formSavedError = resJson.errorMessage;
        }
      });
    },
    async testConfig() {
      this.configTestLoading = true;
      sloConfig.test(this.name, this.data._path).then((resJson) => {
        this.configTestLoading = false;
        if (resJson.success) {
          this.configTestSuccess = true;
          this.configTestSuccessMessage = "Config validated succesfully !";
          this.configTestData = resJson.data
        } else {
          this.configTestSuccess = false
          this.configTestErrorMessage = resJson.errorMessage
          this.configTestTraceback = resJson.traceback
        }
      });
    },
    async fetchGitDiff() {
      sloConfig.diff(this.name).then((resJson) => {
        this.sloGitDiff = resJson.diff.replace(new RegExp("\n", "g"), "<br>");
      });
    },
  },
  mixins: [fmtMixin],
  components: {
    SLOCard,
    SLOForm,
  },
});
</script>
