SyncCursorPage[ThreadMessage](
    data=[
        ThreadMessage(
            id="msg_1eSUH4KPxAH36ZvSW3aTRIPt",
            assistant_id="asst_CDrvSIEoSCbOomSOh2zHmqL6",
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value="The sections that contain tables related to investment schedule, investment amount, and similar information, along with the associated page numbers, are:\n\n- Schedule of Portfolio Investments【11†source】: Page 3.\n- Concentration of Investments【17†source】: This information begins on page 11 and continues onto page 12.",
                    ),
                    type="text",
                )
            ],
            created_at=1699450102,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="assistant",
            run_id="run_LEV2MTlsls1UJdgYd804bXJ6",
            thread_id="thread_qY6sVsajSLo5kXOXmAd9cdIU",
        ),
        ThreadMessage(
            id="msg_8dUsXBdHGeChMrbnT7O6jidY",
            assistant_id=None,
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value="what sections contain tables related to investment schedule/investment amount etc.\n                   You can either return the section heading or the page_numbers associated with the tables",
                    ),
                    type="text",
                )
            ],
            created_at=1699450087,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="user",
            run_id=None,
            thread_id="thread_qY6sVsajSLo5kXOXmAd9cdIU",
        ),
    ],
    object="list",
    first_id="msg_1eSUH4KPxAH36ZvSW3aTRIPt",
    last_id="msg_8dUsXBdHGeChMrbnT7O6jidY",
    has_more=False,
)
ThreadMessage(
    id="msg_CLQnR1hp7BjxwqLVcP7gy5Qh",
    assistant_id=None,
    content=[
        MessageContentText(
            text=Text(
                annotations=[], value="can you extract more such tables' sources?"
            ),
            type="text",
        )
    ],
    created_at=1699452357,
    file_ids=[],
    metadata={},
    object="thread.message",
    role="user",
    run_id=None,
    thread_id="thread_qY6sVsajSLo5kXOXmAd9cdIU",
)
Run(
    id="run_a6tcUlCNnUrMpfaOfi4KwD3u",
    assistant_id="asst_lnDHDp0kz8iJBhkpkhqUSGTy",
    cancelled_at=None,
    completed_at=None,
    created_at=1699531958,
    expires_at=1699532558,
    failed_at=None,
    file_ids=["file-5ZO5cWOHxbYOTftnFWEtToaH", "file-8i9vVMHiPAwnVXYuCnGLYocu"],
    instructions="\n                      You are an intelligent assistant capable of understanding financial pdf files.\n                      You are an expert at guiding the user to the correct pages regarding their queries.\n                      You are comprehensive in your answer and will extract all possible sources that relates to the user's question.\n                      ",
    last_error=None,
    metadata={},
    model="gpt-4-1106-preview",
    object="thread.run",
    required_action=RequiredAction(
        submit_tool_outputs=RequiredActionSubmitToolOutputs(
            tool_calls=[
                RequiredActionFunctionToolCall(
                    id="call_Bn97iAX953MkQI03x5zK9RQv",
                    function=Function(
                        arguments='{"pdf": "Mercer.pdf"}', name="extract_source"
                    ),
                    type="function",
                ),
                RequiredActionFunctionToolCall(
                    id="call_1N23RME5ntSj4oVOUBskBpj6",
                    function=Function(
                        arguments='{"pdf": "DarwinVCFinStatements.pdf"}',
                        name="extract_source",
                    ),
                    type="function",
                ),
            ]
        ),
        type="submit_tool_outputs",
    ),
    started_at=1699531958,
    status="requires_action",
    thread_id="thread_EHPQjQzHNvXIta6SVf3seZIX",
    tools=[
        ToolAssistantToolsFunction(
            function=ToolAssistantToolsFunctionFunction(
                description="Get the pdf name and the contents associated with it",
                name="extract_source",
                parameters={
                    "type": "object",
                    "properties": {
                        "pdf": {"type": "string", "description": "The pdf name"},
                        "contents": {
                            "type": "string",
                            "description": "Content associated with it",
                        },
                    },
                    "required": ["pdf_source", "page_number"],
                },
            ),
            type="function",
        ),
        ToolAssistantToolsRetrieval(type="retrieval"),
    ],
)
[
    RunStep(
        id="step_e8Dnt3ygFcoQbqdqocpioNAR",
        assistant_id="asst_lnDHDp0kz8iJBhkpkhqUSGTy",
        cancelled_at=None,
        completed_at=1699535211,
        created_at=1699535109,
        expired_at=None,
        failed_at=None,
        last_error=None,
        metadata=None,
        object="thread.run.step",
        run_id="run_I0HxFrM6mn22RV9KV0Jumj8P",
        status="completed",
        step_details=ToolCallsStepDetails(
            tool_calls=[
                RetrievalToolCall(
                    id="call_ulxn5Ebfemc5tHv1lx9hIXjE", retrieval={}, type="retrieval"
                )
            ],
            type="tool_calls",
        ),
        thread_id="thread_zZsD7jAE70cPUm8BO67oWmFZ",
        type="tool_calls",
        expires_at=None,
    )
]

SyncCursorPage[ThreadMessage](
    data=[
        ThreadMessage(
            id="msg_MJUrYkiFNnYg4F2qkSOoHeCA",
            assistant_id="asst_lnDHDp0kz8iJBhkpkhqUSGTy",
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value='In the "Mercer.pdf" file, tables related to the user\'s query regarding investment schedules, investment commitments, remaining commitments, and capital deployed were found on the following pages:\n\n**Investment Schedule and Commitment**\n- Table titled "Schedule of Changes in Partners’ Capital Accounts (Unaudited)" presents a breakdown of capital commitments, capital contributions, distributions, partners’ capital, and remaining capital commitments as of June 30, 2017, showing the timetable of when and how much money was to be deployed, money promised to be deployed, and the remaining amount to be deployed【15†source】【35†source】【43†source】.\n\n**Investment Commitment**\n- Table titled "Consolidated Condensed Schedule of Investments" outlines the investment commitment by classes (Class R1 - Infrastructure, Class R2 - Real Estate, Class R3 - Natural Resources), including the original investment commitment, cost, fair value, the percentage of partners’ capital, and the remaining investment commitment as of June 30, 2017【21†source】.\n\n**Remaining Commitment**\n- Additional references to various remaining unfunded commitments in different currencies translated into U.S. dollars as of June 30, 2017, such as British pounds (GBP), Euros (EUR), Australian dollars (AUD), and Canadian dollars (CAD)【27†source】.\n\n**Capital Deployed**\n- The same table titled "Schedule of Changes in Partners’ Capital Accounts (Unaudited)" also details the initial and updated capital contributions as of June 30, 2017, indicative of the amount of money deployed【35†source】.\n\nThere were no accessible tables in the "DarwinVCFinStatements.pdf" file pertaining to the user\'s query as the document could not be opened using the `myfiles_browser` tool. If there are additional steps or alternative means to access the content in "DarwinVCFinStatements.pdf", please inform me so I can assist further.',
                    ),
                    type="text",
                )
            ],
            created_at=1699617511,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="assistant",
            run_id="run_WOF047I0WBWQmdEIWdYf1dPq",
            thread_id="thread_Q5qfjl1FBPdOGGdb7HQGRRhD",
        ),
        ThreadMessage(
            id="msg_mgKZnpy53NlnVVtbVVEi6Jsm",
            assistant_id=None,
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value=" return all pages that contain tables that have anything to do with the following:\n                    investment schedule: time table of when and how much money is to be deployed \n                    investment commitment: Money promised to be deployed \n                    remaining commitment: Remaining amount to be deployed \n                    capital deployed: Amount of money deployed. \n                    Ensure to return the table's heading and columns as source. \n                    Ensure to do this for the follwing files: -Mercer.pdf -DarwinVCFinStatements.pdf\n                    ",
                    ),
                    type="text",
                )
            ],
            created_at=1699617461,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="user",
            run_id=None,
            thread_id="thread_Q5qfjl1FBPdOGGdb7HQGRRhD",
        ),
    ],
    object="list",
    first_id="msg_MJUrYkiFNnYg4F2qkSOoHeCA",
    last_id="msg_mgKZnpy53NlnVVtbVVEi6Jsm",
    has_more=False,
)
SyncCursorPage[ThreadMessage](
    data=[
        ThreadMessage(
            id="msg_iBSYhH9n0oBOk3QGvEMlrcR1",
            assistant_id=None,
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value="Do  this for -DarwinVCFinStatements.pdf as well",
                    ),
                    type="text",
                )
            ],
            created_at=1699619210,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="user",
            run_id=None,
            thread_id="thread_Q5qfjl1FBPdOGGdb7HQGRRhD",
        ),
        ThreadMessage(
            id="msg_MJUrYkiFNnYg4F2qkSOoHeCA",
            assistant_id="asst_lnDHDp0kz8iJBhkpkhqUSGTy",
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value='In the "Mercer.pdf" file, tables related to the user\'s query regarding investment schedules, investment commitments, remaining commitments, and capital deployed were found on the following pages:\n\n**Investment Schedule and Commitment**\n- Table titled "Schedule of Changes in Partners’ Capital Accounts (Unaudited)" presents a breakdown of capital commitments, capital contributions, distributions, partners’ capital, and remaining capital commitments as of June 30, 2017, showing the timetable of when and how much money was to be deployed, money promised to be deployed, and the remaining amount to be deployed【15†source】【35†source】【43†source】.\n\n**Investment Commitment**\n- Table titled "Consolidated Condensed Schedule of Investments" outlines the investment commitment by classes (Class R1 - Infrastructure, Class R2 - Real Estate, Class R3 - Natural Resources), including the original investment commitment, cost, fair value, the percentage of partners’ capital, and the remaining investment commitment as of June 30, 2017【21†source】.\n\n**Remaining Commitment**\n- Additional references to various remaining unfunded commitments in different currencies translated into U.S. dollars as of June 30, 2017, such as British pounds (GBP), Euros (EUR), Australian dollars (AUD), and Canadian dollars (CAD)【27†source】.\n\n**Capital Deployed**\n- The same table titled "Schedule of Changes in Partners’ Capital Accounts (Unaudited)" also details the initial and updated capital contributions as of June 30, 2017, indicative of the amount of money deployed【35†source】.\n\nThere were no accessible tables in the "DarwinVCFinStatements.pdf" file pertaining to the user\'s query as the document could not be opened using the `myfiles_browser` tool. If there are additional steps or alternative means to access the content in "DarwinVCFinStatements.pdf", please inform me so I can assist further.',
                    ),
                    type="text",
                )
            ],
            created_at=1699617511,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="assistant",
            run_id="run_WOF047I0WBWQmdEIWdYf1dPq",
            thread_id="thread_Q5qfjl1FBPdOGGdb7HQGRRhD",
        ),
        ThreadMessage(
            id="msg_mgKZnpy53NlnVVtbVVEi6Jsm",
            assistant_id=None,
            content=[
                MessageContentText(
                    text=Text(
                        annotations=[],
                        value=" return all pages that contain tables that have anything to do with the following:\n                    investment schedule: time table of when and how much money is to be deployed \n                    investment commitment: Money promised to be deployed \n                    remaining commitment: Remaining amount to be deployed \n                    capital deployed: Amount of money deployed. \n                    Ensure to return the table's heading and columns as source. \n                    Ensure to do this for the follwing files: -Mercer.pdf -DarwinVCFinStatements.pdf\n                    ",
                    ),
                    type="text",
                )
            ],
            created_at=1699617461,
            file_ids=[],
            metadata={},
            object="thread.message",
            role="user",
            run_id=None,
            thread_id="thread_Q5qfjl1FBPdOGGdb7HQGRRhD",
        ),
    ],
    object="list",
    first_id="msg_iBSYhH9n0oBOk3QGvEMlrcR1",
    last_id="msg_mgKZnpy53NlnVVtbVVEi6Jsm",
    has_more=False,
)
{
    "object": "list",
    "data": [
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699617300,
            "n_requests": 20,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 98875,
            "n_generated_tokens_total": 801,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699619100,
            "n_requests": 5,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 36444,
            "n_generated_tokens_total": 210,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629000,
            "n_requests": 50,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 179851,
            "n_generated_tokens_total": 1988,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629300,
            "n_requests": 42,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 146457,
            "n_generated_tokens_total": 1487,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629600,
            "n_requests": 20,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 76500,
            "n_generated_tokens_total": 325,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629900,
            "n_requests": 22,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 75363,
            "n_generated_tokens_total": 793,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699630200,
            "n_requests": 8,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 40543,
            "n_generated_tokens_total": 500,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699630500,
            "n_requests": 24,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 85888,
            "n_generated_tokens_total": 1077,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699630800,
            "n_requests": 33,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 122766,
            "n_generated_tokens_total": 977,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699637700,
            "n_requests": 4,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 7155,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699638000,
            "n_requests": 1,
            "operation": "completion",
            "snapshot_id": "gpt-3.5-turbo-0613",
            "n_context_tokens_total": 19,
            "n_generated_tokens_total": 2,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699638600,
            "n_requests": 1,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 12,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699638600,
            "n_requests": 2,
            "operation": "completion",
            "snapshot_id": "gpt-3.5-turbo-0613",
            "n_context_tokens_total": 2314,
            "n_generated_tokens_total": 252,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699639500,
            "n_requests": 2,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 7150,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699639800,
            "n_requests": 1,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 20,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699639800,
            "n_requests": 3,
            "operation": "completion",
            "snapshot_id": "gpt-3.5-turbo-0613",
            "n_context_tokens_total": 3141,
            "n_generated_tokens_total": 290,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699640100,
            "n_requests": 1,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 1,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
    ],
    "ft_data": [],
    "dalle_api_data": [],
    "whisper_api_data": [],
}
"Fund Investment", "Investment Objective"
"8VC Co-Invest Fund I, L.P.", "Invests in follow-on and co-invest venture capital investments in securities of the companies currently held by one or more of the Core Funds."
"8VC Fund I, L.P.", "Organized for the purpose of making or acquiring portfolio investments."
"Founders Fund IV, L.P. (The)", "Invests in innovative technology companies for long-term capital appreciation."
"Founders Fund V, L.P. (The)", "Invests in early stage, high growth technology companies for long-term capital appreciation."
"Founders Fund VI, L.P. (The)", "Invests in early stage, high growth technology companies for long-term capital appreciation."
"Khosla Ventures V, L.P.", "Invests in early stage technology companies."
"SherpaEverest Fund, L.P.", "Organized for the purpose of making or acquiring portfolio investments."
"SherpaVentures Fund II, L.P.", "Organized for the purpose of making or acquiring portfolio investments."

{
    "object": "list",
    "data": [
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699617300,
            "n_requests": 20,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 98875,
            "n_generated_tokens_total": 801,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699619100,
            "n_requests": 5,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 36444,
            "n_generated_tokens_total": 210,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629000,
            "n_requests": 50,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 179851,
            "n_generated_tokens_total": 1988,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629300,
            "n_requests": 42,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 146457,
            "n_generated_tokens_total": 1487,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629600,
            "n_requests": 20,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 76500,
            "n_generated_tokens_total": 325,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699629900,
            "n_requests": 22,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 75363,
            "n_generated_tokens_total": 793,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699630200,
            "n_requests": 8,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 40543,
            "n_generated_tokens_total": 500,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699630500,
            "n_requests": 24,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 85888,
            "n_generated_tokens_total": 1077,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699630800,
            "n_requests": 33,
            "operation": "completion",
            "snapshot_id": "gpt-4-1106-preview",
            "n_context_tokens_total": 122766,
            "n_generated_tokens_total": 977,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699637700,
            "n_requests": 4,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 7155,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699638000,
            "n_requests": 1,
            "operation": "completion",
            "snapshot_id": "gpt-3.5-turbo-0613",
            "n_context_tokens_total": 19,
            "n_generated_tokens_total": 2,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699638600,
            "n_requests": 1,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 12,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699638600,
            "n_requests": 2,
            "operation": "completion",
            "snapshot_id": "gpt-3.5-turbo-0613",
            "n_context_tokens_total": 2314,
            "n_generated_tokens_total": 252,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699639500,
            "n_requests": 2,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 7150,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699639800,
            "n_requests": 1,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 20,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699639800,
            "n_requests": 3,
            "operation": "completion",
            "snapshot_id": "gpt-3.5-turbo-0613",
            "n_context_tokens_total": 3141,
            "n_generated_tokens_total": 290,
            "user_id": None,
        },
        {
            "organization_id": "org-c09SCHfmnaDL6sfKBJGuuRzF",
            "aggregation_timestamp": 1699640100,
            "n_requests": 1,
            "operation": "embeddings",
            "snapshot_id": "text-embedding-ada-002-v2",
            "n_context_tokens_total": 1,
            "n_generated_tokens_total": 0,
            "user_id": None,
        },
    ],
    "ft_data": [],
    "dalle_api_data": [],
    "whisper_api_data": [],
}
"Venture Fund Partnerships","Investment Commitment","Remaining Commitment"
"8VC Fund I, L.P.","7,000,000","3,750,000"
"8VC Co-Invest Fund I, L.P.","7,500,000","1,750,000"
"First Round Capital IV, L.P.","1,100,000","39,050"
"First Round Capital V, L.P.","1,100,000","220,000"
"Founders Fund IV, L.P. (The)","1,000,000","30,000"
"Founders Fund V, L.P. (The)","5,000,000","100,000"
"Founders Fund VI, L.P. (The)","7,000,000","3,850,000"
"Khosla Ventures Seed C, L.P.","3,000,000","165,000"
"Khosla Ventures V, L.P.","7,000,000","924,000"
"Kleiner Perkins Caufield & Byers XV, LLC","1,000,000","90,000"
"Kleiner Perkins Caufield & Byers XVI, LLC","1,000,000","90,000"
"KPCB Digital Growth Fund III, LLC","1,000,000","97,500"
"Lightspeed Venture Partners Select, L.P.","1,500,000","105,000"
"Lightspeed Ventures Partners X, L.P.","1,500,000","82,500"
"Menlo Ventures XII, L.P.","3,000,000","150,000"
"SherpaEverest Fund, L.P.","6,000,000","780,000"
"SherpaVentures Fund II, L.P.","6,000,000","1,650,000"
"Total at December 31, 2018","60,700,000","13,873,050"