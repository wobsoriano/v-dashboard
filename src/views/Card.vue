<template>
  <div>
    <h3 class="text-3xl font-semibold text-gray-700">
      Card
    </h3>
    <div class="mt-4 mb-3">
      <h4 class="text-gray-700">
        Stacked
      </h4>

      <div class="max-w-sm mt-6 overflow-hidden bg-white rounded shadow-lg">
        <img
          class="w-full"
          src="https://picsum.photos/id/1016/384/234"
          alt="Sunset in the mountains"
        >
        <div class="px-6 py-4">
          <div class="mb-2 text-xl font-bold text-gray-900">
            The Coldest Sunset
          </div>
          <p class="text-base text-gray-700">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Voluptatibus quia, nulla! Maiores et perferendis eaque,
            exercitationem praesentium nihil.
          </p>
        </div>
        <div class="px-6 pt-4 pb-2">
          <span
            class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
          >#photography</span>
          <span
            class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
          >#travel</span>
          <span
            class="inline-block px-3 py-1 mb-2 mr-2 text-sm font-semibold text-gray-700 bg-gray-200 rounded-full"
          >#winter</span>
        </div>
      </div>
    </div>
    <hr>
    <div class="mt-5">
      <h4 class="text-gray-700">
        Horizontal
      </h4>
      <div class="w-full max-w-sm mt-6 lg:max-w-full lg:flex">
        <div
          class="flex-none h-48 overflow-hidden text-center bg-cover rounded-t lg:h-auto lg:w-48 lg:rounded-t-none lg:rounded-l"
          style="background-image: url('https://picsum.photos/id/0/192/213')"
          title="Woman holding a mug"
        />
        <div
          class="flex flex-col justify-between p-4 leading-normal bg-white border-b border-l border-r border-gray-200 rounded-b lg:border-l-0 lg:border-t lg:border-gray-200 lg:rounded-b-none lg:rounded-r"
        >
          <div class="mb-8">
            <p class="flex items-center text-sm text-gray-600">
              <svg
                class="w-3 h-3 mr-2 text-gray-500 fill-current"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z"
                />
              </svg>
              Members only
            </p>
            <div class="mb-2 text-xl font-bold text-gray-900">
              Can coffee make you a better developer?
            </div>
            <p class="text-base text-gray-700">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Voluptatibus quia, nulla! Maiores et perferendis eaque,
              exercitationem praesentium nihil.
            </p>
          </div>
          <div class="flex items-center">
            <img
              class="w-10 h-10 mr-4 rounded-full"
              src="https://via.placeholder.com/50"
              alt="Avatar of Jonathan Reinink"
            >
            <div class="text-sm">
              <p class="leading-none text-gray-900">
                Jonathan Reinink
              </p>
              <p class="text-gray-600">
                Aug 18
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
